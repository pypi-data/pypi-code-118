# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Globalization.DateTimeFormatting")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

class DayFormat(enum.IntEnum):
    NONE = 0
    DEFAULT = 1

class DayOfWeekFormat(enum.IntEnum):
    NONE = 0
    DEFAULT = 1
    ABBREVIATED = 2
    FULL = 3

class HourFormat(enum.IntEnum):
    NONE = 0
    DEFAULT = 1

class MinuteFormat(enum.IntEnum):
    NONE = 0
    DEFAULT = 1

class MonthFormat(enum.IntEnum):
    NONE = 0
    DEFAULT = 1
    ABBREVIATED = 2
    FULL = 3
    NUMERIC = 4

class SecondFormat(enum.IntEnum):
    NONE = 0
    DEFAULT = 1

class YearFormat(enum.IntEnum):
    NONE = 0
    DEFAULT = 1
    ABBREVIATED = 2
    FULL = 3

DateTimeFormatter = _ns_module.DateTimeFormatter
