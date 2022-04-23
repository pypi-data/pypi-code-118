# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.System.Preview")

try:
    import winsdk.windows.devices.sensors
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

class HingeState(enum.IntEnum):
    UNKNOWN = 0
    CLOSED = 1
    CONCAVE = 2
    FLAT = 3
    CONVEX = 4
    FULL = 5

TwoPanelHingedDevicePosturePreview = _ns_module.TwoPanelHingedDevicePosturePreview
TwoPanelHingedDevicePosturePreviewReading = _ns_module.TwoPanelHingedDevicePosturePreviewReading
TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs = _ns_module.TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs
