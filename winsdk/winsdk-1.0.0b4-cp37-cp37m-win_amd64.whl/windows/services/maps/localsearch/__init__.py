# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Services.Maps.LocalSearch")

try:
    import winsdk.windows.devices.geolocation
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.globalization
except Exception:
    pass

try:
    import winsdk.windows.services.maps
except Exception:
    pass

class LocalLocationFinderStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_CREDENTIALS = 2
    INVALID_CATEGORY = 3
    INVALID_SEARCH_TERM = 4
    INVALID_SEARCH_AREA = 5
    NETWORK_FAILURE = 6
    NOT_SUPPORTED = 7

LocalCategories = _ns_module.LocalCategories
LocalLocation = _ns_module.LocalLocation
LocalLocationFinder = _ns_module.LocalLocationFinder
LocalLocationFinderResult = _ns_module.LocalLocationFinderResult
LocalLocationHoursOfOperationItem = _ns_module.LocalLocationHoursOfOperationItem
LocalLocationRatingInfo = _ns_module.LocalLocationRatingInfo
PlaceInfoHelper = _ns_module.PlaceInfoHelper
