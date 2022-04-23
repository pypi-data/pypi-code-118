# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Adc")

try:
    import winsdk.windows.devices.adc.provider
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

class AdcChannelMode(enum.IntEnum):
    SINGLE_ENDED = 0
    DIFFERENTIAL = 1

AdcChannel = _ns_module.AdcChannel
AdcController = _ns_module.AdcController
