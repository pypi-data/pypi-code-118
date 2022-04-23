from __future__ import annotations

from typing import Union

import numpy as np

from ada import Part
from ada.base.physical_objects import BackendGeom
from ada.concepts.curves import CurvePoly
from ada.concepts.primitives import PrimBox
from ada.concepts.transforms import Placement
from ada.core.vector_utils import unit_vector


class WallJustification:
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    all = [CENTER, LEFT, RIGHT]


class Wall(BackendGeom):
    TYPES_JUSL = WallJustification

    """
    A wall object representing

    :param points: Points making up wall
    :param height: Height
    :param thickness: Thickness
    :param origin: Origin
    :param offset: Wall offset from points making up the wall centerline. Accepts float | CENTER | LEFT | RIGHT
    """

    def __init__(
        self,
        name,
        points,
        height,
        thickness,
        placement=Placement(),
        offset=TYPES_JUSL.CENTER,
        metadata=None,
        colour=None,
        ifc_elem=None,
        units="m",
        guid=None,
        opacity=1.0,
    ):
        super().__init__(
            name, guid=guid, metadata=metadata, units=units, ifc_elem=ifc_elem, colour=colour, opacity=opacity
        )

        self._name = name
        self.placement = placement
        self.colour = colour
        new_points = []
        for p in points:
            np_ = [float(c) for c in p]
            if len(np_) == 2:
                np_ += [0.0]
            new_points.append(tuple(np_))
        self._points = new_points
        self._segments = list(zip(self._points[:-1], self.points[1:]))
        self._height = height
        self._thickness = thickness
        self._openings = []
        self._doors = []
        self._inserts = []
        if type(offset) is str:
            if offset not in Wall.TYPES_JUSL.all:
                raise ValueError(f'Unknown string input "{offset}" for offset')
            if offset == Wall.TYPES_JUSL.CENTER:
                self._offset = 0.0
            elif offset == Wall.TYPES_JUSL.LEFT:
                self._offset = -self._thickness / 2
            else:  # offset = RIGHT
                self._offset = self._thickness / 2
        else:
            if type(offset) not in (float, int):
                raise ValueError("Offset can only be string or float, int")
            self._offset = offset

    def add_insert(self, insert: "WallInsert", wall_segment: int, off_x, off_z):
        """

        :param insert:
        :param wall_segment:
        :param off_x:
        :param off_z:
        :return:
        """
        from OCC.Extend.ShapeFactory import get_oriented_boundingbox

        xvec, yvec, zvec = self.get_segment_props(wall_segment)
        p1, p2 = self._segments[wall_segment]

        start = p1 + yvec * (self._thickness / 2 + self.offset) + xvec * off_x + zvec * off_z
        insert._depth = self._thickness
        insert.placement = Placement(origin=start, xdir=xvec, ydir=zvec, zdir=yvec)

        frame = insert.shapes[0]
        center, dim, oobb_shp = get_oriented_boundingbox(frame.geom)
        x, y, z = center.X(), center.Y(), center.Z()
        dx, dy, dz = dim[0], dim[1], dim[2]

        x0 = x - abs(dx / 2)
        y0 = y - abs(dy / 2)
        z0 = z - abs(dz / 2)

        x1 = x + abs(dx / 2)
        y1 = y + abs(dy / 2)
        z1 = z + abs(dz / 2)

        self._inserts.append(insert)
        self._openings.append([wall_segment, insert, (x0, y0, z0), (x1, y1, z1)])

        tol = 0.4
        wi = insert

        p1 = wi.placement.origin - yvec * (wi.depth / 2 + tol)
        p2 = wi.placement.origin + yvec * (wi.depth / 2 + tol) + xvec * wi.width + zvec * wi.height

        self._penetrations.append(PrimBox("my_pen", p1, p2))

    def get_segment_props(self, wall_segment):
        """

        :param wall_segment:
        :return:
        """
        if wall_segment > len(self._segments):
            raise ValueError(f"Wall segment id should be equal or less than {len(self._segments)}")

        p1, p2 = self._segments[wall_segment]
        xvec = unit_vector(np.array(p2) - np.array(p1))
        zvec = np.array([0, 0, 1])
        yvec = unit_vector(np.cross(zvec, xvec))

        return xvec, yvec, zvec

    def _generate_ifc_elem(self):
        from ada.ifc.write.write_wall import write_ifc_wall

        return write_ifc_wall(self)

    @property
    def inserts(self):
        return self._inserts

    @property
    def height(self):
        return self._height

    @property
    def thickness(self):
        return self._thickness

    @property
    def placement(self) -> Placement:
        return self._placement

    @placement.setter
    def placement(self, value: Placement):
        self._placement = value

    @property
    def points(self):
        return self._points

    @property
    def offset(self) -> Union[float, str]:
        return self._offset

    @property
    def extrusion_area(self):
        from ada.core.vector_utils import calc_yvec, intersect_calc, is_parallel

        area_points = []
        vpo = [np.array(p) for p in self.points]
        p2 = None
        yvec = None
        prev_xvec = None
        prev_yvec = None
        zvec = np.array([0, 0, 1])

        # Inner line
        for p1, p2 in zip(vpo[:-1], vpo[1:]):
            xvec = p2 - p1
            yvec = unit_vector(calc_yvec(xvec, zvec))
            new_point = p1 + yvec * (self._thickness / 2) + yvec * self.offset
            if prev_xvec is not None:
                if is_parallel(xvec, prev_xvec) is False:
                    prev_p = area_points[-1]
                    # next_point = p2 + yvec * (self._thickness / 2) + yvec * self.offset
                    # c_p = prev_yvec * (self._thickness / 2) + prev_yvec * self.offset
                    AB = prev_xvec
                    CD = xvec
                    s, t = intersect_calc(prev_p, new_point, AB, CD)
                    sAB = prev_p + s * AB
                    new_point = sAB
            area_points.append(new_point)
            prev_xvec = xvec
            prev_yvec = yvec

        # Add last point
        area_points.append((p2 + yvec * (self._thickness / 2) + yvec * self.offset))
        area_points.append((p2 - yvec * (self._thickness / 2) + yvec * self.offset))

        reverse_points = []
        # Outer line
        prev_xvec = None
        prev_yvec = None
        for p1, p2 in zip(vpo[:-1], vpo[1:]):
            xvec = p2 - p1
            yvec = unit_vector(calc_yvec(xvec, zvec))
            new_point = p1 - yvec * (self._thickness / 2) + yvec * self.offset
            if prev_xvec is not None:
                if is_parallel(xvec, prev_xvec) is False:
                    prev_p = reverse_points[-1]
                    c_p = prev_yvec * (self._thickness / 2) - prev_yvec * self.offset
                    new_point -= c_p
            reverse_points.append(new_point)
            prev_xvec = xvec
            prev_yvec = yvec

        reverse_points.reverse()
        area_points += reverse_points

        new_points = []
        for p in area_points:
            new_points.append(tuple([float(c) for c in p]))

        return new_points

    @property
    def openings_extrusions(self):
        from ada.concepts.levels import Part

        op_extrudes = []
        if self.units == "m":
            tol = 0.4
        else:
            tol = 400
        for op in self._openings:
            ws, wi, mi, ma = op
            xvec, yvec, zvec = self.get_segment_props(ws)
            assert issubclass(type(wi), Part)
            p1 = wi.placement.origin - yvec * (wi.depth / 2 + tol)
            p2 = p1 + yvec * (wi.depth + tol * 2)
            p3 = p2 + xvec * wi.width
            p4 = p3 - yvec * (wi.depth + tol * 2)
            op_extrudes.append([p1.tolist(), p2.tolist(), p3.tolist(), p4.tolist(), p1.tolist()])
        return op_extrudes

    @property
    def metadata(self):
        return self._metadata

    @property
    def shell(self):
        poly = CurvePoly(points3d=self.extrusion_area, parent=self)
        return poly.face

    @property
    def solid(self):
        from ada.occ.utils import apply_penetrations

        poly = CurvePoly(points3d=self.extrusion_area, parent=self)

        geom = apply_penetrations(poly.make_extruded_solid(self.height), self.penetrations)

        return geom

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        if value != self._units:
            from ada.core.utils import unit_length_conversion

            scale_factor = unit_length_conversion(self._units, value)
            self._height *= scale_factor
            self._thickness *= scale_factor
            self._offset *= scale_factor
            self.placement.origin = np.array([x * scale_factor for x in self.placement.origin])
            self._points = [tuple([x * scale_factor for x in p]) for p in self.points]
            self._segments = list(zip(self._points[:-1], self.points[1:]))
            for pen in self._penetrations:
                pen.units = value
            for opening in self._openings:
                opening[2] = tuple([x * scale_factor for x in opening[2]])
                opening[3] = tuple([x * scale_factor for x in opening[3]])

            for insert in self._inserts:
                insert.units = value

            self._units = value

    def __repr__(self):
        return f"Wall({self.name})"


class WallInsert(Part):
    def __init__(self, name, width, height, depth, **kwargs):
        super(WallInsert, self).__init__(name, **kwargs)
        self._width = width
        self._height = height
        self._depth = depth
        self._is_built = False

    def build_geom(self):
        raise NotImplementedError()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def depth(self):
        return self._depth

    @property
    def placement(self):
        return self._placement

    @placement.setter
    def placement(self, value):
        self._placement = value
        self.build_geom()
        self._is_built = True
