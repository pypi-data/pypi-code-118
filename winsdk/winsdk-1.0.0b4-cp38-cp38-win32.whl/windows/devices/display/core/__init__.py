# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Display.Core")

try:
    import winsdk.windows.devices.display
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
    import winsdk.windows.foundation.numerics
except Exception:
    pass

try:
    import winsdk.windows.graphics
except Exception:
    pass

try:
    import winsdk.windows.graphics.directx
except Exception:
    pass

try:
    import winsdk.windows.graphics.directx.direct3d11
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class DisplayBitsPerChannel(enum.IntFlag):
    NONE = 0
    BPC6 = 0x1
    BPC8 = 0x2
    BPC10 = 0x4
    BPC12 = 0x8
    BPC14 = 0x10
    BPC16 = 0x20

class DisplayDeviceCapability(enum.IntEnum):
    FLIP_OVERRIDE = 0

class DisplayManagerOptions(enum.IntFlag):
    NONE = 0
    ENFORCE_SOURCE_OWNERSHIP = 0x1
    VIRTUAL_REFRESH_RATE_AWARE = 0x2

class DisplayManagerResult(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_FAILURE = 1
    TARGET_ACCESS_DENIED = 2
    TARGET_STALE = 3
    REMOTE_SESSION_NOT_SUPPORTED = 4

class DisplayModeQueryOptions(enum.IntFlag):
    NONE = 0
    ONLY_PREFERRED_RESOLUTION = 0x1

class DisplayPathScaling(enum.IntEnum):
    IDENTITY = 0
    CENTERED = 1
    STRETCHED = 2
    ASPECT_RATIO_STRETCHED = 3
    CUSTOM = 4
    DRIVER_PREFERRED = 5

class DisplayPathStatus(enum.IntEnum):
    UNKNOWN = 0
    SUCCEEDED = 1
    PENDING = 2
    FAILED = 3
    FAILED_ASYNC = 4
    INVALIDATED_ASYNC = 5

class DisplayPresentStatus(enum.IntEnum):
    SUCCESS = 0
    SOURCE_STATUS_PREVENTED_PRESENT = 1
    SCANOUT_INVALID = 2
    SOURCE_INVALID = 3
    DEVICE_INVALID = 4
    UNKNOWN_FAILURE = 5

class DisplayRotation(enum.IntEnum):
    NONE = 0
    CLOCKWISE90_DEGREES = 1
    CLOCKWISE180_DEGREES = 2
    CLOCKWISE270_DEGREES = 3

class DisplayScanoutOptions(enum.IntFlag):
    NONE = 0
    ALLOW_TEARING = 0x2

class DisplaySourceStatus(enum.IntEnum):
    ACTIVE = 0
    POWERED_OFF = 1
    INVALID = 2
    OWNED_BY_ANOTHER_DEVICE = 3
    UNOWNED = 4

class DisplayStateApplyOptions(enum.IntFlag):
    NONE = 0
    FAIL_IF_STATE_CHANGED = 0x1
    FORCE_REAPPLY = 0x2
    FORCE_MODE_ENUMERATION = 0x4

class DisplayStateFunctionalizeOptions(enum.IntFlag):
    NONE = 0
    FAIL_IF_STATE_CHANGED = 0x1
    VALIDATE_TOPOLOGY_ONLY = 0x2

class DisplayStateOperationStatus(enum.IntEnum):
    SUCCESS = 0
    PARTIAL_FAILURE = 1
    UNKNOWN_FAILURE = 2
    TARGET_OWNERSHIP_LOST = 3
    SYSTEM_STATE_CHANGED = 4
    TOO_MANY_PATHS_FOR_ADAPTER = 5
    MODES_NOT_SUPPORTED = 6
    REMOTE_SESSION_NOT_SUPPORTED = 7

class DisplayTargetPersistence(enum.IntEnum):
    NONE = 0
    BOOT_PERSISTED = 1
    TEMPORARY_PERSISTED = 2
    PATH_PERSISTED = 3

class DisplayTaskSignalKind(enum.IntEnum):
    ON_PRESENT_FLIP_AWAY = 0
    ON_PRESENT_FLIP_TO = 1

class DisplayWireFormatColorSpace(enum.IntEnum):
    B_T709 = 0
    B_T2020 = 1
    PROFILE_DEFINED_WIDE_COLOR_GAMUT = 2

class DisplayWireFormatEotf(enum.IntEnum):
    SDR = 0
    HDR_SMPTE2084 = 1

class DisplayWireFormatHdrMetadata(enum.IntEnum):
    NONE = 0
    HDR10 = 1
    HDR10_PLUS = 2
    DOLBY_VISION_LOW_LATENCY = 3

class DisplayWireFormatPixelEncoding(enum.IntEnum):
    RGB444 = 0
    YCC444 = 1
    YCC422 = 2
    YCC420 = 3
    INTENSITY = 4

DisplayPresentationRate = _ns_module.DisplayPresentationRate
DisplayAdapter = _ns_module.DisplayAdapter
DisplayDevice = _ns_module.DisplayDevice
DisplayFence = _ns_module.DisplayFence
DisplayManager = _ns_module.DisplayManager
DisplayManagerChangedEventArgs = _ns_module.DisplayManagerChangedEventArgs
DisplayManagerDisabledEventArgs = _ns_module.DisplayManagerDisabledEventArgs
DisplayManagerEnabledEventArgs = _ns_module.DisplayManagerEnabledEventArgs
DisplayManagerPathsFailedOrInvalidatedEventArgs = _ns_module.DisplayManagerPathsFailedOrInvalidatedEventArgs
DisplayManagerResultWithState = _ns_module.DisplayManagerResultWithState
DisplayModeInfo = _ns_module.DisplayModeInfo
DisplayPath = _ns_module.DisplayPath
DisplayPrimaryDescription = _ns_module.DisplayPrimaryDescription
DisplayScanout = _ns_module.DisplayScanout
DisplaySource = _ns_module.DisplaySource
DisplayState = _ns_module.DisplayState
DisplayStateOperationResult = _ns_module.DisplayStateOperationResult
DisplaySurface = _ns_module.DisplaySurface
DisplayTarget = _ns_module.DisplayTarget
DisplayTask = _ns_module.DisplayTask
DisplayTaskPool = _ns_module.DisplayTaskPool
DisplayTaskResult = _ns_module.DisplayTaskResult
DisplayView = _ns_module.DisplayView
DisplayWireFormat = _ns_module.DisplayWireFormat
