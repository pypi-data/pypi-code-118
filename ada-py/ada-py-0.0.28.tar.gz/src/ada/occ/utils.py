import logging
import math
import pathlib
from typing import TYPE_CHECKING, List, Tuple, Union

import numpy as np
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRep import BRep_Tool_Pnt
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBndLib import brepbndlib_Add
from OCC.Core.BRepBuilderAPI import (
    BRepBuilderAPI_MakeEdge,
    BRepBuilderAPI_MakeFace,
    BRepBuilderAPI_MakePolygon,
    BRepBuilderAPI_MakeWire,
    BRepBuilderAPI_Transform,
)
from OCC.Core.BRepExtrema import BRepExtrema_DistShapeShape
from OCC.Core.BRepFill import BRepFill_Filling
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakePipe, BRepOffsetAPI_ThruSections
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.ChFi2d import ChFi2d_AnaFilletAlgo
from OCC.Core.GC import GC_MakeArcOfCircle
from OCC.Core.GeomAbs import GeomAbs_C0
from OCC.Core.gp import gp_Ax1, gp_Ax2, gp_Circ, gp_Dir, gp_Pln, gp_Pnt, gp_Trsf, gp_Vec
from OCC.Core.ShapeUpgrade import ShapeUpgrade_UnifySameDomain
from OCC.Core.TopoDS import (
    TopoDS_Compound,
    TopoDS_Edge,
    TopoDS_Face,
    TopoDS_Shape,
    TopoDS_Shell,
    TopoDS_Solid,
    TopoDS_Vertex,
    TopoDS_Wire,
)
from OCC.Extend.DataExchange import read_step_file
from OCC.Extend.ShapeFactory import make_extrusion, make_face, make_wire
from OCC.Extend.TopologyUtils import TopologyExplorer

from ada.concepts.primitives import Penetration
from ada.concepts.stru_beams import Beam
from ada.concepts.transforms import Placement, Rotation
from ada.core.utils import roundoff, tuple_minus
from ada.core.vector_utils import unit_vector, vector_length
from ada.fem.shapes import ElemType

from .exceptions.geom_creation import (
    UnableToBuildNSidedWires,
    UnableToCreateSolidOCCGeom,
)

if TYPE_CHECKING:
    from ada import Part


def extract_shapes(step_path, scale, transform, rotate):
    shapes = []

    cad_file_path = pathlib.Path(step_path)
    if cad_file_path.is_file():
        shapes += extract_subshapes(read_step_file(str(cad_file_path), as_compound=False))
    elif cad_file_path.is_dir():
        shapes += walk_shapes(cad_file_path)
    else:
        raise Exception(f'step_ref "{step_path}" does not represent neither file or folder found on system')

    shapes = [transform_shape(s, scale, transform, rotate) for s in shapes]
    return shapes


def transform_shape(
    shape: Union[TopoDS_Shape], scale=None, transform: Union[Placement, tuple, list] = None, rotate: Rotation = None
) -> TopoDS_Shape:

    trsf = gp_Trsf()
    if scale is not None:
        trsf.SetScaleFactor(scale)
    if transform is not None:
        if type(transform) is Placement:
            tra = transform.origin
            trsf.SetTranslation(gp_Vec(tra[0], tra[1], tra[2]))
        elif type(transform) in (tuple, list):
            trsf.SetTranslation(gp_Vec(transform[0], transform[1], transform[2]))
        else:
            raise ValueError(f'Unrecognized transform input type "{type(transform)}"')
    if rotate is not None:
        pt = gp_Pnt(*rotate.origin)
        dire = gp_Dir(*rotate.vector)
        revolve_axis = gp_Ax1(pt, dire)
        trsf.SetRotation(revolve_axis, math.radians(rotate.angle))
    return BRepBuilderAPI_Transform(shape, trsf, True).Shape()


def walk_shapes(dir_path):
    from ..core.file_system import get_list_of_files

    shps = []
    for stp_file in get_list_of_files(dir_path, ".stp"):
        shps += extract_subshapes(read_step_file(stp_file))
    return shps


def extract_subshapes(shp_):
    t = TopologyExplorer(shp_)
    return list(t.solids())


def is_edges_ok(edge1, fillet, edge2):
    t1 = TopologyExplorer(edge1).number_of_vertices()
    t2 = TopologyExplorer(fillet).number_of_vertices()
    t3 = TopologyExplorer(edge2).number_of_vertices()

    if t1 == 0 or t2 == 0 or t3 == 0:
        return False
    else:
        return True


def make_wire_from_points(points):
    if type(points[0]) in (list, tuple):
        p1 = list(points[0])
        p2 = list(points[1])
    else:
        p1 = points[0].tolist()
        p2 = points[1].tolist()

    if len(p1) == 2:
        p1 += [0]
        p2 += [0]

    return make_wire([BRepBuilderAPI_MakeEdge(gp_Pnt(*p1), gp_Pnt(*p2)).Edge()])


def get_boundingbox(shape: TopoDS_Shape, tol=1e-6, use_mesh=True) -> Tuple[tuple, tuple]:
    """

    :param shape: TopoDS_Shape or a subclass such as TopoDS_Face the shape to compute the bounding box from
    :param tol: tolerance of the computed boundingbox
    :param use_mesh: a flag that tells whether or not the shape has first to be meshed before the bbox computation.
                     This produces more accurate results
    :return: return the bounding box of the TopoDS_Shape `shape`
    """

    bbox = Bnd_Box()
    bbox.SetGap(tol)
    if use_mesh:
        mesh = BRepMesh_IncrementalMesh()
        mesh.SetParallelDefault(True)
        mesh.SetShape(shape)
        mesh.Perform()
        if not mesh.IsDone():
            raise AssertionError("Mesh not done.")
    brepbndlib_Add(shape, bbox, use_mesh)

    xmin, ymin, zmin, xmax, ymax, zmax = bbox.Get()
    return (xmin, ymin, zmin), (xmax, ymax, zmax)


def get_bounding_box_alt(geom):
    from OCC.Core.Bnd import Bnd_OBB
    from OCC.Core.BRepBndLib import brepbndlib_AddOBB

    obb = Bnd_OBB()
    brepbndlib_AddOBB(geom, obb)

    # converts the bounding box to a shape
    # aBaryCenter = obb.Center()
    # aXDir = obb.XDirection()
    # aYDir = obb.YDirection()
    # aZDir = obb.ZDirection()
    # aHalfX = obb.XHSize()
    # aHalfY = obb.YHSize()
    # aHalfZ = obb.ZHSize()
    return obb


def is_occ_shape(shp):
    """

    :param shp:
    :return:
    """
    if type(shp) in [
        TopoDS_Shell,
        TopoDS_Vertex,
        TopoDS_Solid,
        TopoDS_Wire,
        TopoDS_Shape,
        TopoDS_Compound,
    ]:
        return True
    else:
        return False


def face_to_wires(face):
    topo_exp = TopologyExplorer(face)
    wires = list()
    for w in topo_exp.wires_from_face(face):
        wires.append(w)
    return wires


def make_fillet(edge1, edge2, bend_radius):
    from ada.core.vector_utils import normal_to_points_in_plane

    f = ChFi2d_AnaFilletAlgo()

    points1 = get_points_from_edge(edge1)
    points2 = get_points_from_edge(edge2)
    normal = normal_to_points_in_plane([np.array(x) for x in points1] + [np.array(x) for x in points2])
    plane_normal = gp_Dir(gp_Vec(normal[0], normal[1], normal[2]))

    t = TopologyExplorer(edge1)
    apt = None
    for v in t.vertices():
        apt = BRep_Tool_Pnt(v)

    f.Init(edge1, edge2, gp_Pln(apt, plane_normal))
    f.Perform(bend_radius)
    fillet2d = f.Result(edge1, edge2)
    if is_edges_ok(edge1, fillet2d, edge2) is False:
        raise ValueError("Unsuccessful filleting of edges")

    return edge1, edge2, fillet2d


def get_midpoint_of_arc(edge):
    res = divide_edge_by_nr_of_points(edge, 3)
    return res[1][1].X(), res[1][1].Y(), res[1][1].Z()


def divide_edge_by_nr_of_points(edg, n_pts):
    from OCC.Core.BRepAdaptor import BRepAdaptor_Curve
    from OCC.Core.GCPnts import GCPnts_UniformAbscissa

    """returns a nested list of parameters and points on the edge
    at the requested interval [(param, gp_Pnt),...]
    """
    curve_adapt = BRepAdaptor_Curve(edg)
    _lbound, _ubound = curve_adapt.FirstParameter(), curve_adapt.LastParameter()

    if n_pts <= 1:
        # minimally two points or a Standard_ConstructionError is raised
        raise AssertionError("minimally 2 points required")

    npts = GCPnts_UniformAbscissa(curve_adapt, n_pts, _lbound, _ubound)
    if npts.IsDone():
        tmp = []
        for i in range(1, npts.NbPoints() + 1):
            param = npts.Parameter(i)
            pnt = curve_adapt.Value(param)
            tmp.append((param, pnt))
        return tmp


def get_points_from_edge(edge):
    texp1 = TopologyExplorer(edge)
    points = []
    for v in texp1.vertices():
        apt = BRep_Tool_Pnt(v)
        points.append((apt.X(), apt.Y(), apt.Z()))
    return points


def make_closed_polygon(*args):
    poly = BRepBuilderAPI_MakePolygon()
    for pt in args:
        if isinstance(pt, list) or isinstance(pt, tuple):
            for i in pt:
                poly.Add(i)
        else:
            poly.Add(pt)
    poly.Build()
    poly.Close()
    result = poly.Wire()
    return result


def make_face_w_cutout(face: TopoDS_Face, wire_cutout: TopoDS_Wire) -> TopoDS_Face:
    wire_cutout.Reverse()
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeFace

    return BRepBuilderAPI_MakeFace(face, wire_cutout).Face()


def make_circle(p, vec, r):
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
    from OCC.Core.gp import gp_Ax2, gp_Circ, gp_Dir, gp_Pnt

    circle_origin = gp_Ax2(gp_Pnt(p[0], p[1], p[2]), gp_Dir(vec[0], vec[1], vec[2]))
    circle = gp_Circ(circle_origin, r)

    return BRepBuilderAPI_MakeEdge(circle).Edge()


def make_box(origin_pnt, dx, dy, dz, sf=1.0):
    """
    The variable origin_pnt can be a dict with the format of {'X': XXX, 'Y': YYY , 'Z': ZZZ}, ADA Node object or
    a simple list, dx, dy and dz are floats.

    The origin_pnt represents the bottom corner of the box whereas dx, dy and dz are distances from that bottom
    corner point describing the entire volume.

    :param origin_pnt:
    :param dx:
    :param dy:
    :param dz:
    :param sf: Scale Factor
    :type dx: float
    :type dy: float
    :type dz: float

    """
    from ada import Node

    if type(origin_pnt) is Node:
        assert isinstance(origin_pnt, Node)
        aPnt1 = gp_Pnt(float(origin_pnt.x) * sf, float(origin_pnt.y) * sf, float(origin_pnt.z) * sf)
    elif type(origin_pnt) == dict:
        aPnt1 = gp_Pnt(
            float(origin_pnt["X"]) * sf,
            float(origin_pnt["Y"]) * sf,
            float(origin_pnt["Z"]) * sf,
        )
    elif type(origin_pnt) == list or type(origin_pnt) == tuple or type(origin_pnt) is np.ndarray:
        origin_pnt = [roundoff(x * sf) for x in list(origin_pnt)]
        aPnt1 = gp_Pnt(float(origin_pnt[0]), float(origin_pnt[1]), float(origin_pnt[2]))
    else:
        raise ValueError(f"Unknown input format {origin_pnt}")

    my_box = BRepPrimAPI_MakeBox(aPnt1, dx * sf, dy * sf, dz * sf).Shape()
    return my_box


def make_box_by_points(p1, p2, scale=1.0):
    from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
    from OCC.Core.gp import gp_Pnt

    if type(p1) == list or type(p1) == tuple or type(p1) is np.ndarray:
        deltas = [roundoff((p2_ - p1_) * scale) for p1_, p2_ in zip(p1, p2)]
        p1_in = [roundoff(x * scale) for x in p1]

    else:
        raise ValueError("Unknown input format {type(p1)}")

    dx = deltas[0]
    dy = deltas[1]
    dz = deltas[2]

    gp = gp_Pnt(p1_in[0], p1_in[1], p1_in[2])

    return BRepPrimAPI_MakeBox(gp, dx, dy, dz).Shape()


def make_cylinder(p, vec, h, r, t=None):
    """

    :param p:
    :param vec:
    :param h:
    :param r:
    :param t: Wall thickness (if applicable). Will make a
    :return:
    """
    cylinder_origin = gp_Ax2(gp_Pnt(p[0], p[1], p[2]), gp_Dir(vec[0], vec[1], vec[2]))
    cylinder = BRepPrimAPI_MakeCylinder(cylinder_origin, r, h).Shape()
    if t is not None:
        cutout = BRepPrimAPI_MakeCylinder(cylinder_origin, r - t, h).Shape()
        return BRepAlgoAPI_Cut(cylinder, cutout).Shape()
    else:
        return cylinder


def make_cylinder_from_points(p1, p2, r, t=None):
    vec = unit_vector(np.array(p2) - np.array(p1))
    l = vector_length(np.array(p2) - np.array(p1))
    return make_cylinder(p1, vec, l, r, t)


def make_sphere(pnt, radius):
    """
    Create a sphere using coordinates (x,y,z) and radius.

    :param pnt: Point
    :param radius: Radius
    """
    from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere
    from OCC.Core.gp import gp_Pnt

    aPnt1 = gp_Pnt(float(pnt[0]), float(pnt[1]), float(pnt[2]))
    Sphere = BRepPrimAPI_MakeSphere(aPnt1, radius).Shape()
    return Sphere


def make_revolved_cylinder(pnt, height, revolve_angle, rotation, wall_thick):
    """
    This method demonstrates how to create a revolved shape from a drawn closed edge.
    It currently creates a hollow cylinder

    adapted from algotopia.com's opencascade_basic tutorial:
    http://www.algotopia.com/contents/opencascade/opencascade_basic

    :param pnt:
    :param height:
    :param revolve_angle:
    :param rotation:
    :param wall_thick:
    :type pnt: dict
    :type height: float
    :type revolve_angle: float
    :type rotation: float
    :type wall_thick: float
    """
    from OCC.Core.BRepBuilderAPI import (
        BRepBuilderAPI_MakeEdge,
        BRepBuilderAPI_MakeFace,
        BRepBuilderAPI_MakeWire,
    )
    from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeRevol
    from OCC.Core.gp import gp_Ax1, gp_Dir, gp_Pnt

    face_inner_radius = pnt["X"] + (17.0 - wall_thick / 2) * 1000
    face_outer_radius = pnt["X"] + (17.0 + wall_thick / 2) * 1000

    # point to create an edge from
    edg_points = [
        gp_Pnt(face_inner_radius, pnt["Y"], pnt["Z"]),
        gp_Pnt(face_inner_radius, pnt["Y"], pnt["Z"] + height),
        gp_Pnt(face_outer_radius, pnt["Y"], pnt["Z"] + height),
        gp_Pnt(face_outer_radius, pnt["Y"], pnt["Z"]),
        gp_Pnt(face_inner_radius, pnt["Y"], pnt["Z"]),
    ]

    # aggregate edges in wire
    hexwire = BRepBuilderAPI_MakeWire()

    for i in range(len(edg_points) - 1):
        hexedge = BRepBuilderAPI_MakeEdge(edg_points[i], edg_points[i + 1]).Edge()
        hexwire.Add(hexedge)

    hexwire_wire = hexwire.Wire()
    # face from wire
    hexface = BRepBuilderAPI_MakeFace(hexwire_wire).Face()
    revolve_axis = gp_Ax1(gp_Pnt(pnt["X"], pnt["Y"], pnt["Z"]), gp_Dir(0, 0, 1))
    # create revolved shape
    revolved_shape_ = BRepPrimAPI_MakeRevol(hexface, revolve_axis, np.radians(float(revolve_angle))).Shape()
    revolved_shape_ = rotate_shp_3_axis(revolved_shape_, revolve_axis, rotation)

    return revolved_shape_


def make_edge(p1, p2):
    """

    :param p1:
    :param p2:
    :type p1: tuple
    :type p2: tuple

    :return:
    :rtype: OCC.Core.TopoDS.TopoDS_Edge
    """
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
    from OCC.Core.gp import gp_Pnt

    p1 = gp_Pnt(*[float(x) for x in p1[:3]])
    p2 = gp_Pnt(*[float(x) for x in p2[:3]])
    res = BRepBuilderAPI_MakeEdge(p1, p2).Edge()

    if res.IsNull():
        logging.debug("Edge creation returned None")

    return res


def make_ori_vector(
    name, origin, csys, pnt_r=0.02, cyl_l: Union[float, list, tuple] = 0.3, cyl_r=0.02, units="m"
) -> "Part":
    """
    Visualize a local coordinate system with a sphere and 3 cylinders representing origin and.

    :param name:
    :param origin:
    :param csys: Coordinate system
    :param pnt_r:
    :param cyl_l:
    :type cyl_l: Union[float, list, tuple]
    :param cyl_r:
    :param units:
    :return:
    """
    from ada import Part, PrimCyl, PrimSphere

    origin = np.array(origin)
    o_shape = PrimSphere(name + "_origin", origin, pnt_r, units=units, metadata=dict(origin=origin), colour="white")

    if type(cyl_l) in (list, tuple):
        cyl_l_x, cyl_l_y, cyl_l_z = cyl_l
    else:
        cyl_l_x, cyl_l_y, cyl_l_z = cyl_l, cyl_l, cyl_l

    x_vec_shape = PrimCyl(
        name + "_X",
        origin,
        origin + np.array(csys[0]) * cyl_l_x,
        cyl_r,
        units=units,
        colour="BLUE",
    )

    y_vec_shape = PrimCyl(
        name + "_Y",
        origin,
        origin + np.array(csys[1]) * cyl_l_y,
        cyl_r,
        units=units,
        colour="GREEN",
    )

    z_vec_shape = PrimCyl(
        name + "_Z",
        origin,
        origin + np.array(csys[2]) * cyl_l_z,
        cyl_r,
        units=units,
        colour="RED",
    )
    return Part(name, units=units) / (o_shape, x_vec_shape, y_vec_shape, z_vec_shape)


def visualize_elem_ori(elem):
    """

    :param elem:
    :type elem: ada.fem.Elem
    :return: ada.Shape
    """
    origin = (elem.nodes[-1].p + elem.nodes[0].p) / 2
    return make_ori_vector(
        f"elem{elem.id}_ori",
        origin,
        elem.fem_sec.csys,
        pnt_r=0.2,
        cyl_r=0.05,
        cyl_l=1.0,
        units=elem.fem_sec.section.units,
    )


def visualize_load(load, units="m", pnt_r=0.2, cyl_r=0.05, cyl_l_norm=1.5):
    """

    :param load:
    :param units:
    :param pnt_r:
    :param cyl_r:
    :param cyl_l_norm:
    :type load: ada.fem.Load
    :return:
    :rtype: ada.Part
    """
    from ada.core.constants import X, Y, Z

    csys = load.csys if load.csys is not None else [X, Y, Z]
    forces = np.array(load.forces[:3])
    forces_normalized = tuple(cyl_l_norm * (forces / max(abs(forces))))

    origin = load.fem_set.members[0].p

    return make_ori_vector(
        f"F_{load.name}_ori",
        origin,
        csys,
        pnt_r=pnt_r,
        cyl_r=cyl_r,
        cyl_l=forces_normalized,
        units=units,
    )


def get_edge_points(edge):
    from OCC.Core.BRep import BRep_Tool_Pnt
    from OCC.Extend.TopologyUtils import TopologyExplorer

    t = TopologyExplorer(edge)
    points = []
    for v in t.vertices():
        apt = BRep_Tool_Pnt(v)
        points.append((apt.X(), apt.Y(), apt.Z()))
    return points


def rotate_shp_3_axis(shape, revolve_axis, rotation):
    """
    Rotate a shape around a pre-defined rotation axis gp_Ax1.

    @param rotation : rotation in degrees around (gp_Ax1)
    @param shape : shape in question
    @param revolve_axis : rotation axis gp_Ax1
    @return : the rotated shape.
    """
    alpha = gp_Trsf()
    alpha.SetRotation(revolve_axis, np.deg2rad(rotation))
    brep_trns = BRepBuilderAPI_Transform(shape, alpha, False)
    shp = brep_trns.Shape()
    return shp


def compute_minimal_distance_between_shapes(shp1, shp2) -> BRepExtrema_DistShapeShape:
    """Compute the minimal distance between 2 shapes"""

    dss = BRepExtrema_DistShapeShape()
    dss.LoadS1(shp1)
    dss.LoadS2(shp2)
    dss.Perform()

    assert dss.IsDone()

    logging.info("Minimal distance between shapes: ", dss.Value())

    return dss


def make_circular_sec_wire(point: gp_Pnt, direction: gp_Dir, radius) -> TopoDS_Wire:
    circle = gp_Circ(gp_Ax2(point, direction), radius)
    profile_edge = BRepBuilderAPI_MakeEdge(circle).Edge()
    return BRepBuilderAPI_MakeWire(profile_edge).Wire()


def make_circular_sec_face(point: gp_Pnt, direction: gp_Dir, radius) -> TopoDS_Face:
    profile_wire = make_circular_sec_wire(point, direction, radius)
    return BRepBuilderAPI_MakeFace(profile_wire).Face()


def sweep_pipe(edge, xvec, r, wt, geom_repr=ElemType.SOLID):
    if geom_repr not in [ElemType.SOLID, ElemType.SHELL]:
        raise ValueError("Sweeping pipe must be either 'solid' or 'shell'")

    t = TopologyExplorer(edge)
    points = [v for v in t.vertices()]
    point = BRep_Tool_Pnt(points[0])
    # x, y, z = point.X(), point.Y(), point.Z()
    direction = gp_Dir(*unit_vector(xvec).astype(float).tolist())

    # pipe
    makeWire = BRepBuilderAPI_MakeWire()
    makeWire.Add(edge)
    makeWire.Build()
    wire = makeWire.Wire()
    try:
        if geom_repr == ElemType.SOLID:
            i = make_circular_sec_face(point, direction, r - wt)
            elbow_i = BRepOffsetAPI_MakePipe(wire, i).Shape()
            o = make_circular_sec_face(point, direction, r)
            elbow_o = BRepOffsetAPI_MakePipe(wire, o).Shape()
        else:
            elbow_i = None
            o = make_circular_sec_wire(point, direction, r)
            elbow_o = BRepOffsetAPI_MakePipe(wire, o).Shape()
    except RuntimeError as e:
        logging.error(f'Pipe sweep failed: "{e}"')
        return wire
    if geom_repr == ElemType.SOLID:
        boolean_result = BRepAlgoAPI_Cut(elbow_o, elbow_i).Shape()
        if boolean_result.IsNull():
            logging.debug("Boolean returns None")
    else:
        boolean_result = elbow_o

    return boolean_result


def sweep_geom(sweep_wire: TopoDS_Wire, wire_face: TopoDS_Wire):
    return BRepOffsetAPI_MakePipe(sweep_wire, wire_face).Shape()


def build_polycurve_occ(local_points, input_2d_coords=False, tol=1e-3):
    """

    :param local_points:
    :param input_2d_coords:
    :return: List of segments
    """
    from ada import ArcSegment, LineSegment

    if input_2d_coords:
        local_points = [(x[0], x[1], 0.0) if len(x) == 2 else (x[0], x[1], 0.0, x[2]) for x in local_points]

    edges = []
    pzip = list(zip(local_points[:-1], local_points[1:]))
    segs = [[p1, p2] for p1, p2 in pzip]
    segs += [segs[0]]
    segzip = list(zip(segs[:-1], segs[1:]))
    seg_list = []
    for i, (seg1, seg2) in enumerate(segzip):
        p11, p12 = seg1
        p21, p22 = seg2

        if i == 0:
            edge1 = make_edge(p11[:3], p12[:3])
        else:
            edge1 = edges[-1]
        if i == len(segzip) - 1:
            endp = seg_list[0].midpoint if type(seg_list[0]) is ArcSegment else seg_list[0].p2
            edge2 = make_edge(seg_list[0].p1, endp)
        else:
            edge2 = make_edge(p21[:3], p22[:3])

        if len(p21) > 3:
            r = p21[-1]

            tseg1 = get_edge_points(edge1)
            tseg2 = get_edge_points(edge2)

            l1_start = tseg1[0]
            l2_end = tseg2[1]

            ed1, ed2, fillet = make_fillet(edge1, edge2, r)

            seg1 = get_edge_points(ed1)
            seg2 = get_edge_points(ed2)
            arc_start = seg1[1]
            arc_end = seg2[0]
            midpoint = get_midpoint_of_arc(fillet)

            if i == 0:
                edges.append(ed1)
                seg_list.append(LineSegment(p1=l1_start, p2=arc_start))

            seg_list[-1].p2 = arc_start
            edges.append(fillet)

            seg_list.append(ArcSegment(p1=arc_start, p2=arc_end, midpoint=midpoint))
            if i == len(segzip) - 1:
                seg_list[0].p1 = arc_end
                edges[0] = ed2
            else:
                edges.append(ed2)
                seg_list.append(LineSegment(p1=arc_end, p2=l2_end))
        else:
            if i == 0:
                edges.append(edge1)
                seg_list.append(LineSegment(p1=p11, p2=p12))
            if i < len(segzip) - 1:
                edges.append(edge2)
                seg_list.append(LineSegment(p1=p21, p2=p22))
    return seg_list


def create_beam_geom(beam: Beam, solid=True):
    from ada.concepts.transforms import Placement
    from ada.sections.categories import SectionCat

    from .section_utils import cross_sec_face

    xdir, ydir, zdir = beam.ori
    ydir_neg = tuple_minus(ydir) if beam.section.type not in SectionCat.angular else tuple(ydir)

    section_profile = beam.section.get_section_profile(solid)
    taper_profile = beam.taper.get_section_profile(solid)

    placement_1 = Placement(origin=beam.n1.p, xdir=ydir_neg, zdir=xdir)
    placement_2 = Placement(origin=beam.n2.p, xdir=ydir_neg, zdir=xdir)

    sec = cross_sec_face(section_profile, placement_1, solid)
    tap = cross_sec_face(taper_profile, placement_2, solid)

    if type(sec) != list and (sec.IsNull() or tap.IsNull()):
        raise UnableToCreateSolidOCCGeom(f"Unable to create solid OCC geometry from Beam '{beam.name}'")

    def through_section(sec_a, sec_b, solid_):
        generator_sec = BRepOffsetAPI_ThruSections(solid_, False)
        generator_sec.AddWire(sec_a)
        generator_sec.AddWire(sec_b)
        generator_sec.Build()
        return generator_sec.Shape()

    if type(sec) is TopoDS_Face:
        sec_result = face_to_wires(sec)
        tap_result = face_to_wires(tap)
    elif type(sec) is TopoDS_Wire:
        sec_result = [sec]
        tap_result = [tap]
    else:
        try:
            assert isinstance(sec, list)
        except AssertionError as e:
            logging.error(e)
        sec_result = sec
        tap_result = tap

    shapes = list()
    for s_, t_ in zip(sec_result, tap_result):
        shapes.append(through_section(s_, t_, solid))

    if beam.section.type in SectionCat.box + SectionCat.tubular + SectionCat.rhs + SectionCat.shs and solid is True:
        cut_shape = BRepAlgoAPI_Cut(shapes[0], shapes[1]).Shape()
        shape_upgrade = ShapeUpgrade_UnifySameDomain(cut_shape, False, True, False)
        shape_upgrade.Build()
        return shape_upgrade.Shape()

    if len(shapes) == 1:
        return shapes[0]
    else:
        result = shapes[0]
        for s in shapes[1:]:
            result = BRepAlgoAPI_Fuse(result, s).Shape()
        return result


def apply_penetrations(geom: TopoDS_Shape, penetrations: List[Penetration]) -> TopoDS_Shape:
    for pen in penetrations:
        geom = BRepAlgoAPI_Cut(geom, pen.geom).Shape()

    return geom


def segments_to_edges(segments) -> List[TopoDS_Edge]:
    from ada.concepts.curves import ArcSegment

    edges = []
    for seg in segments:
        if type(seg) is ArcSegment:
            a_arc_of_circle = GC_MakeArcOfCircle(
                gp_Pnt(*list(seg.p1)),
                gp_Pnt(*list(seg.midpoint)),
                gp_Pnt(*list(seg.p2)),
            )
            a_edge2 = BRepBuilderAPI_MakeEdge(a_arc_of_circle.Value()).Edge()
            edges.append(a_edge2)
        else:
            edge = make_edge(seg.p1, seg.p2)
            edges.append(edge)

    return edges


def extrude_closed_wire(wire: TopoDS_Wire, origin, normal, height) -> TopoDS_Shape:
    """Extrude a closed wire into a solid"""
    p1 = origin + normal * height
    starting_point = gp_Pnt(origin[0], origin[1], origin[2])
    end_point = gp_Pnt(*p1.tolist())
    vec = gp_Vec(starting_point, end_point)

    solid = make_extrusion(make_face(wire), height, vec)

    return solid


def make_revolve_solid(face: TopoDS_Face, axis, angle, origin) -> TopoDS_Shape:
    from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeRevol

    revolve_axis = gp_Ax1(gp_Pnt(origin[0], origin[1], origin[2]), gp_Dir(axis[0], axis[1], axis[2]))
    revolved_shape = BRepPrimAPI_MakeRevol(face, revolve_axis, np.deg2rad(angle)).Shape()
    return revolved_shape


def wire_to_face(edges: List[TopoDS_Edge]) -> TopoDS_Face:
    n_sided = BRepFill_Filling()
    for edg in edges:
        n_sided.Add(edg, GeomAbs_C0)
    try:
        n_sided.Build()
    except RuntimeError as e:
        raise UnableToBuildNSidedWires(e)
    face = n_sided.Face()
    return face
