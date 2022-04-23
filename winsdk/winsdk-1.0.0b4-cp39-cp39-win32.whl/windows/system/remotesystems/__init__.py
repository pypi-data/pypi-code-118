# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.System.RemoteSystems")

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
    import winsdk.windows.networking
except Exception:
    pass

try:
    import winsdk.windows.security.credentials
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

class RemoteSystemAccessStatus(enum.IntEnum):
    UNSPECIFIED = 0
    ALLOWED = 1
    DENIED_BY_USER = 2
    DENIED_BY_SYSTEM = 3

class RemoteSystemAuthorizationKind(enum.IntEnum):
    SAME_USER = 0
    ANONYMOUS = 1

class RemoteSystemDiscoveryType(enum.IntEnum):
    ANY = 0
    PROXIMAL = 1
    CLOUD = 2
    SPATIALLY_PROXIMAL = 3

class RemoteSystemPlatform(enum.IntEnum):
    UNKNOWN = 0
    WINDOWS = 1
    ANDROID = 2
    IOS = 3
    LINUX = 4

class RemoteSystemSessionCreationStatus(enum.IntEnum):
    SUCCESS = 0
    SESSION_LIMITS_EXCEEDED = 1
    OPERATION_ABORTED = 2

class RemoteSystemSessionDisconnectedReason(enum.IntEnum):
    SESSION_UNAVAILABLE = 0
    REMOVED_BY_CONTROLLER = 1
    SESSION_CLOSED = 2

class RemoteSystemSessionJoinStatus(enum.IntEnum):
    SUCCESS = 0
    SESSION_LIMITS_EXCEEDED = 1
    OPERATION_ABORTED = 2
    SESSION_UNAVAILABLE = 3
    REJECTED_BY_CONTROLLER = 4

class RemoteSystemSessionMessageChannelReliability(enum.IntEnum):
    RELIABLE = 0
    UNRELIABLE = 1

class RemoteSystemSessionParticipantWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

class RemoteSystemSessionWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

class RemoteSystemStatus(enum.IntEnum):
    UNAVAILABLE = 0
    DISCOVERING_AVAILABILITY = 1
    AVAILABLE = 2
    UNKNOWN = 3

class RemoteSystemStatusType(enum.IntEnum):
    ANY = 0
    AVAILABLE = 1

class RemoteSystemWatcherError(enum.IntEnum):
    UNKNOWN = 0
    INTERNET_NOT_AVAILABLE = 1
    AUTHENTICATION_ERROR = 2

KnownRemoteSystemCapabilities = _ns_module.KnownRemoteSystemCapabilities
RemoteSystem = _ns_module.RemoteSystem
RemoteSystemAddedEventArgs = _ns_module.RemoteSystemAddedEventArgs
RemoteSystemApp = _ns_module.RemoteSystemApp
RemoteSystemAppRegistration = _ns_module.RemoteSystemAppRegistration
RemoteSystemAuthorizationKindFilter = _ns_module.RemoteSystemAuthorizationKindFilter
RemoteSystemConnectionInfo = _ns_module.RemoteSystemConnectionInfo
RemoteSystemConnectionRequest = _ns_module.RemoteSystemConnectionRequest
RemoteSystemDiscoveryTypeFilter = _ns_module.RemoteSystemDiscoveryTypeFilter
RemoteSystemEnumerationCompletedEventArgs = _ns_module.RemoteSystemEnumerationCompletedEventArgs
RemoteSystemKindFilter = _ns_module.RemoteSystemKindFilter
RemoteSystemKinds = _ns_module.RemoteSystemKinds
RemoteSystemRemovedEventArgs = _ns_module.RemoteSystemRemovedEventArgs
RemoteSystemSession = _ns_module.RemoteSystemSession
RemoteSystemSessionAddedEventArgs = _ns_module.RemoteSystemSessionAddedEventArgs
RemoteSystemSessionController = _ns_module.RemoteSystemSessionController
RemoteSystemSessionCreationResult = _ns_module.RemoteSystemSessionCreationResult
RemoteSystemSessionDisconnectedEventArgs = _ns_module.RemoteSystemSessionDisconnectedEventArgs
RemoteSystemSessionInfo = _ns_module.RemoteSystemSessionInfo
RemoteSystemSessionInvitation = _ns_module.RemoteSystemSessionInvitation
RemoteSystemSessionInvitationListener = _ns_module.RemoteSystemSessionInvitationListener
RemoteSystemSessionInvitationReceivedEventArgs = _ns_module.RemoteSystemSessionInvitationReceivedEventArgs
RemoteSystemSessionJoinRequest = _ns_module.RemoteSystemSessionJoinRequest
RemoteSystemSessionJoinRequestedEventArgs = _ns_module.RemoteSystemSessionJoinRequestedEventArgs
RemoteSystemSessionJoinResult = _ns_module.RemoteSystemSessionJoinResult
RemoteSystemSessionMessageChannel = _ns_module.RemoteSystemSessionMessageChannel
RemoteSystemSessionOptions = _ns_module.RemoteSystemSessionOptions
RemoteSystemSessionParticipant = _ns_module.RemoteSystemSessionParticipant
RemoteSystemSessionParticipantAddedEventArgs = _ns_module.RemoteSystemSessionParticipantAddedEventArgs
RemoteSystemSessionParticipantRemovedEventArgs = _ns_module.RemoteSystemSessionParticipantRemovedEventArgs
RemoteSystemSessionParticipantWatcher = _ns_module.RemoteSystemSessionParticipantWatcher
RemoteSystemSessionRemovedEventArgs = _ns_module.RemoteSystemSessionRemovedEventArgs
RemoteSystemSessionUpdatedEventArgs = _ns_module.RemoteSystemSessionUpdatedEventArgs
RemoteSystemSessionValueSetReceivedEventArgs = _ns_module.RemoteSystemSessionValueSetReceivedEventArgs
RemoteSystemSessionWatcher = _ns_module.RemoteSystemSessionWatcher
RemoteSystemStatusTypeFilter = _ns_module.RemoteSystemStatusTypeFilter
RemoteSystemUpdatedEventArgs = _ns_module.RemoteSystemUpdatedEventArgs
RemoteSystemWatcher = _ns_module.RemoteSystemWatcher
RemoteSystemWatcherErrorOccurredEventArgs = _ns_module.RemoteSystemWatcherErrorOccurredEventArgs
RemoteSystemWebAccountFilter = _ns_module.RemoteSystemWebAccountFilter
IRemoteSystemFilter = _ns_module.IRemoteSystemFilter
