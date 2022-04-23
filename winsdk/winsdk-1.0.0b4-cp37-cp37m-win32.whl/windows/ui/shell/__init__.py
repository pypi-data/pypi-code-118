# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.UI.Shell")

try:
    import winsdk.windows.applicationmodel.core
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.ui
except Exception:
    pass

try:
    import winsdk.windows.ui.startscreen
except Exception:
    pass

class ShareWindowCommand(enum.IntEnum):
    NONE = 0
    START_SHARING = 1
    STOP_SHARING = 2

AdaptiveCardBuilder = _ns_module.AdaptiveCardBuilder
ShareWindowCommandEventArgs = _ns_module.ShareWindowCommandEventArgs
ShareWindowCommandSource = _ns_module.ShareWindowCommandSource
TaskbarManager = _ns_module.TaskbarManager
IAdaptiveCard = _ns_module.IAdaptiveCard
IAdaptiveCardBuilderStatics = _ns_module.IAdaptiveCardBuilderStatics
