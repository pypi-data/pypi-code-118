__all__ = (
    "cg",
    "create_ecoinvent_collections",
    "create_empty_intersection",
    "create_restofworlds_collections",
    "create_world_collections",
    "divide_by_area",
    "extension_tables",
    "ExtensionTable",
    "ExtensionTablesLCA",
    "geocollections",
    "get_spatial_dataset_kind",
    "hash_collection",
    "import_from_pandarus",
    "import_regionalized_cfs",
    "Intersection",
    "calculate_intersection",
    "intersections",
    "label_activity_geocollections",
    "Loading",
    "loadings",
    "OneSpatialScaleLCA",
    "PandarusRemote",
    "remote",
    "reset_all_geo",
    "reset_geo_meta",
    "sha256",
    "topocollections",
    "Topography",
    "TwoSpatialScalesLCA",
    "TwoSpatialScalesWithGenericLoadingLCA",
    "raster_as_extension_table",
)

from .version import version as __version__

# ignore future warning from pandas that we can't fix
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from constructive_geometries import ConstructiveGeometries

cg = ConstructiveGeometries()

from bw2data import config

from .topography import Topography
from .loading import Loading
from .meta import (
    extension_tables,
    geocollections,
    intersections,
    loadings,
    topocollections,
)
from .intersection import Intersection
from .xtables import ExtensionTable

from .databases import label_activity_geocollections
from .density import divide_by_area
from .hashing import sha256
from .lca import (
    ExtensionTablesLCA,
    OneSpatialScaleLCA,
    TwoSpatialScalesLCA,
    TwoSpatialScalesWithGenericLoadingLCA,
)

from .pandarus import import_from_pandarus
from .pandarus_remote import remote, PandarusRemote
from .utils import (
    create_empty_intersection,
    get_spatial_dataset_kind,
    hash_collection,
    import_regionalized_cfs,
    reset_all_geo,
    reset_geo_meta,
)
from .base_data import (
    create_ecoinvent_collections,
    create_world_collections,
    create_restofworlds_collections,
)
from .gis_tasks import raster_as_extension_table, calculate_intersection

config.metadata.extend(
    [extension_tables, geocollections, topocollections, intersections, loadings]
)
