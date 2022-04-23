# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Graphics.Display.Core")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

class HdmiDisplayColorSpace(enum.IntEnum):
    RGB_LIMITED = 0
    RGB_FULL = 1
    B_T2020 = 2
    B_T709 = 3

class HdmiDisplayHdrOption(enum.IntEnum):
    NONE = 0
    EOTF_SDR = 1
    EOTF2084 = 2
    DOLBY_VISION_LOW_LATENCY = 3

class HdmiDisplayPixelEncoding(enum.IntEnum):
    RGB444 = 0
    YCC444 = 1
    YCC422 = 2
    YCC420 = 3

HdmiDisplayHdr2086Metadata = _ns_module.HdmiDisplayHdr2086Metadata
HdmiDisplayInformation = _ns_module.HdmiDisplayInformation
HdmiDisplayMode = _ns_module.HdmiDisplayMode
