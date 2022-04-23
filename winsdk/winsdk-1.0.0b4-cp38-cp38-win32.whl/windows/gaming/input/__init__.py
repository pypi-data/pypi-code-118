# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Gaming.Input")

try:
    import winsdk.windows.devices.haptics
except Exception:
    pass

try:
    import winsdk.windows.devices.power
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
    import winsdk.windows.gaming.input.forcefeedback
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

class ArcadeStickButtons(enum.IntFlag):
    NONE = 0
    STICK_UP = 0x1
    STICK_DOWN = 0x2
    STICK_LEFT = 0x4
    STICK_RIGHT = 0x8
    ACTION1 = 0x10
    ACTION2 = 0x20
    ACTION3 = 0x40
    ACTION4 = 0x80
    ACTION5 = 0x100
    ACTION6 = 0x200
    SPECIAL1 = 0x400
    SPECIAL2 = 0x800

class FlightStickButtons(enum.IntFlag):
    NONE = 0
    FIRE_PRIMARY = 0x1
    FIRE_SECONDARY = 0x2

class GameControllerButtonLabel(enum.IntEnum):
    NONE = 0
    XBOX_BACK = 1
    XBOX_START = 2
    XBOX_MENU = 3
    XBOX_VIEW = 4
    XBOX_UP = 5
    XBOX_DOWN = 6
    XBOX_LEFT = 7
    XBOX_RIGHT = 8
    XBOX_A = 9
    XBOX_B = 10
    XBOX_X = 11
    XBOX_Y = 12
    XBOX_LEFT_BUMPER = 13
    XBOX_LEFT_TRIGGER = 14
    XBOX_LEFT_STICK_BUTTON = 15
    XBOX_RIGHT_BUMPER = 16
    XBOX_RIGHT_TRIGGER = 17
    XBOX_RIGHT_STICK_BUTTON = 18
    XBOX_PADDLE1 = 19
    XBOX_PADDLE2 = 20
    XBOX_PADDLE3 = 21
    XBOX_PADDLE4 = 22
    MODE = 23
    SELECT = 24
    MENU = 25
    VIEW = 26
    BACK = 27
    START = 28
    OPTIONS = 29
    SHARE = 30
    UP = 31
    DOWN = 32
    LEFT = 33
    RIGHT = 34
    LETTER_A = 35
    LETTER_B = 36
    LETTER_C = 37
    LETTER_L = 38
    LETTER_R = 39
    LETTER_X = 40
    LETTER_Y = 41
    LETTER_Z = 42
    CROSS = 43
    CIRCLE = 44
    SQUARE = 45
    TRIANGLE = 46
    LEFT_BUMPER = 47
    LEFT_TRIGGER = 48
    LEFT_STICK_BUTTON = 49
    LEFT1 = 50
    LEFT2 = 51
    LEFT3 = 52
    RIGHT_BUMPER = 53
    RIGHT_TRIGGER = 54
    RIGHT_STICK_BUTTON = 55
    RIGHT1 = 56
    RIGHT2 = 57
    RIGHT3 = 58
    PADDLE1 = 59
    PADDLE2 = 60
    PADDLE3 = 61
    PADDLE4 = 62
    PLUS = 63
    MINUS = 64
    DOWN_LEFT_ARROW = 65
    DIAL_LEFT = 66
    DIAL_RIGHT = 67
    SUSPENSION = 68

class GameControllerSwitchKind(enum.IntEnum):
    TWO_WAY = 0
    FOUR_WAY = 1
    EIGHT_WAY = 2

class GameControllerSwitchPosition(enum.IntEnum):
    CENTER = 0
    UP = 1
    UP_RIGHT = 2
    RIGHT = 3
    DOWN_RIGHT = 4
    DOWN = 5
    DOWN_LEFT = 6
    LEFT = 7
    UP_LEFT = 8

class GamepadButtons(enum.IntFlag):
    NONE = 0
    MENU = 0x1
    VIEW = 0x2
    A = 0x4
    B = 0x8
    X = 0x10
    Y = 0x20
    D_PAD_UP = 0x40
    D_PAD_DOWN = 0x80
    D_PAD_LEFT = 0x100
    D_PAD_RIGHT = 0x200
    LEFT_SHOULDER = 0x400
    RIGHT_SHOULDER = 0x800
    LEFT_THUMBSTICK = 0x1000
    RIGHT_THUMBSTICK = 0x2000
    PADDLE1 = 0x4000
    PADDLE2 = 0x8000
    PADDLE3 = 0x10000
    PADDLE4 = 0x20000

class OptionalUINavigationButtons(enum.IntFlag):
    NONE = 0
    CONTEXT1 = 0x1
    CONTEXT2 = 0x2
    CONTEXT3 = 0x4
    CONTEXT4 = 0x8
    PAGE_UP = 0x10
    PAGE_DOWN = 0x20
    PAGE_LEFT = 0x40
    PAGE_RIGHT = 0x80
    SCROLL_UP = 0x100
    SCROLL_DOWN = 0x200
    SCROLL_LEFT = 0x400
    SCROLL_RIGHT = 0x800

class RacingWheelButtons(enum.IntFlag):
    NONE = 0
    PREVIOUS_GEAR = 0x1
    NEXT_GEAR = 0x2
    D_PAD_UP = 0x4
    D_PAD_DOWN = 0x8
    D_PAD_LEFT = 0x10
    D_PAD_RIGHT = 0x20
    BUTTON1 = 0x40
    BUTTON2 = 0x80
    BUTTON3 = 0x100
    BUTTON4 = 0x200
    BUTTON5 = 0x400
    BUTTON6 = 0x800
    BUTTON7 = 0x1000
    BUTTON8 = 0x2000
    BUTTON9 = 0x4000
    BUTTON10 = 0x8000
    BUTTON11 = 0x10000
    BUTTON12 = 0x20000
    BUTTON13 = 0x40000
    BUTTON14 = 0x80000
    BUTTON15 = 0x100000
    BUTTON16 = 0x200000

class RequiredUINavigationButtons(enum.IntFlag):
    NONE = 0
    MENU = 0x1
    VIEW = 0x2
    ACCEPT = 0x4
    CANCEL = 0x8
    UP = 0x10
    DOWN = 0x20
    LEFT = 0x40
    RIGHT = 0x80

ArcadeStickReading = _ns_module.ArcadeStickReading
FlightStickReading = _ns_module.FlightStickReading
GamepadReading = _ns_module.GamepadReading
GamepadVibration = _ns_module.GamepadVibration
RacingWheelReading = _ns_module.RacingWheelReading
UINavigationReading = _ns_module.UINavigationReading
ArcadeStick = _ns_module.ArcadeStick
FlightStick = _ns_module.FlightStick
Gamepad = _ns_module.Gamepad
Headset = _ns_module.Headset
RacingWheel = _ns_module.RacingWheel
RawGameController = _ns_module.RawGameController
UINavigationController = _ns_module.UINavigationController
IGameController = _ns_module.IGameController
IGameControllerBatteryInfo = _ns_module.IGameControllerBatteryInfo
