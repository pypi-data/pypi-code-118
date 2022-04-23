# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Media")

try:
    import winsdk.windows.applicationmodel.appservice
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
    import winsdk.windows.graphics.directx
except Exception:
    pass

try:
    import winsdk.windows.graphics.directx.direct3d11
except Exception:
    pass

try:
    import winsdk.windows.graphics.imaging
except Exception:
    pass

try:
    import winsdk.windows.storage
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class AudioBufferAccessMode(enum.IntEnum):
    READ = 0
    READ_WRITE = 1
    WRITE = 2

class AudioProcessing(enum.IntEnum):
    DEFAULT = 0
    RAW = 1

class MediaPlaybackAutoRepeatMode(enum.IntEnum):
    NONE = 0
    TRACK = 1
    LIST = 2

class MediaPlaybackStatus(enum.IntEnum):
    CLOSED = 0
    CHANGING = 1
    STOPPED = 2
    PLAYING = 3
    PAUSED = 4

class MediaPlaybackType(enum.IntEnum):
    UNKNOWN = 0
    MUSIC = 1
    VIDEO = 2
    IMAGE = 3

class MediaTimelineControllerState(enum.IntEnum):
    PAUSED = 0
    RUNNING = 1
    STALLED = 2
    ERROR = 3

class SoundLevel(enum.IntEnum):
    MUTED = 0
    LOW = 1
    FULL = 2

class SystemMediaTransportControlsButton(enum.IntEnum):
    PLAY = 0
    PAUSE = 1
    STOP = 2
    RECORD = 3
    FAST_FORWARD = 4
    REWIND = 5
    NEXT = 6
    PREVIOUS = 7
    CHANNEL_UP = 8
    CHANNEL_DOWN = 9

class SystemMediaTransportControlsProperty(enum.IntEnum):
    SOUND_LEVEL = 0

MediaTimeRange = _ns_module.MediaTimeRange
AudioBuffer = _ns_module.AudioBuffer
AudioFrame = _ns_module.AudioFrame
AutoRepeatModeChangeRequestedEventArgs = _ns_module.AutoRepeatModeChangeRequestedEventArgs
ImageDisplayProperties = _ns_module.ImageDisplayProperties
MediaExtensionManager = _ns_module.MediaExtensionManager
MediaMarkerTypes = _ns_module.MediaMarkerTypes
MediaProcessingTriggerDetails = _ns_module.MediaProcessingTriggerDetails
MediaTimelineController = _ns_module.MediaTimelineController
MediaTimelineControllerFailedEventArgs = _ns_module.MediaTimelineControllerFailedEventArgs
MusicDisplayProperties = _ns_module.MusicDisplayProperties
PlaybackPositionChangeRequestedEventArgs = _ns_module.PlaybackPositionChangeRequestedEventArgs
PlaybackRateChangeRequestedEventArgs = _ns_module.PlaybackRateChangeRequestedEventArgs
ShuffleEnabledChangeRequestedEventArgs = _ns_module.ShuffleEnabledChangeRequestedEventArgs
SystemMediaTransportControls = _ns_module.SystemMediaTransportControls
SystemMediaTransportControlsButtonPressedEventArgs = _ns_module.SystemMediaTransportControlsButtonPressedEventArgs
SystemMediaTransportControlsDisplayUpdater = _ns_module.SystemMediaTransportControlsDisplayUpdater
SystemMediaTransportControlsPropertyChangedEventArgs = _ns_module.SystemMediaTransportControlsPropertyChangedEventArgs
SystemMediaTransportControlsTimelineProperties = _ns_module.SystemMediaTransportControlsTimelineProperties
VideoDisplayProperties = _ns_module.VideoDisplayProperties
VideoEffects = _ns_module.VideoEffects
VideoFrame = _ns_module.VideoFrame
IMediaExtension = _ns_module.IMediaExtension
IMediaFrame = _ns_module.IMediaFrame
IMediaMarker = _ns_module.IMediaMarker
IMediaMarkers = _ns_module.IMediaMarkers
