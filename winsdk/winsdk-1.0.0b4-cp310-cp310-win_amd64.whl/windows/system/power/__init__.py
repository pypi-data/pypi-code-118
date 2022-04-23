# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.System.Power")

try:
    import winsdk.windows.foundation
except Exception:
    pass

class BatteryStatus(enum.IntEnum):
    NOT_PRESENT = 0
    DISCHARGING = 1
    IDLE = 2
    CHARGING = 3

class EnergySaverStatus(enum.IntEnum):
    DISABLED = 0
    OFF = 1
    ON = 2

class PowerSupplyStatus(enum.IntEnum):
    NOT_PRESENT = 0
    INADEQUATE = 1
    ADEQUATE = 2

BackgroundEnergyManager = _ns_module.BackgroundEnergyManager
ForegroundEnergyManager = _ns_module.ForegroundEnergyManager
PowerManager = _ns_module.PowerManager
