# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Storage.Provider")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
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

class CachedFileOptions(enum.IntFlag):
    NONE = 0
    REQUIRE_UPDATE_ON_ACCESS = 0x1
    USE_CACHED_FILE_WHEN_OFFLINE = 0x2
    DENY_ACCESS_WHEN_OFFLINE = 0x4

class CachedFileTarget(enum.IntEnum):
    LOCAL = 0
    REMOTE = 1

class FileUpdateStatus(enum.IntEnum):
    INCOMPLETE = 0
    COMPLETE = 1
    USER_INPUT_NEEDED = 2
    CURRENTLY_UNAVAILABLE = 3
    FAILED = 4
    COMPLETE_AND_RENAMED = 5

class ReadActivationMode(enum.IntEnum):
    NOT_NEEDED = 0
    BEFORE_ACCESS = 1

class StorageProviderHardlinkPolicy(enum.IntFlag):
    NONE = 0
    ALLOWED = 0x1

class StorageProviderHydrationPolicy(enum.IntEnum):
    PARTIAL = 0
    PROGRESSIVE = 1
    FULL = 2
    ALWAYS_FULL = 3

class StorageProviderHydrationPolicyModifier(enum.IntFlag):
    NONE = 0
    VALIDATION_REQUIRED = 0x1
    STREAMING_ALLOWED = 0x2
    AUTO_DEHYDRATION_ALLOWED = 0x4
    ALLOW_FULL_RESTART_HYDRATION = 0x8

class StorageProviderInSyncPolicy(enum.IntFlag):
    DEFAULT = 0
    FILE_CREATION_TIME = 0x1
    FILE_READ_ONLY_ATTRIBUTE = 0x2
    FILE_HIDDEN_ATTRIBUTE = 0x4
    FILE_SYSTEM_ATTRIBUTE = 0x8
    DIRECTORY_CREATION_TIME = 0x10
    DIRECTORY_READ_ONLY_ATTRIBUTE = 0x20
    DIRECTORY_HIDDEN_ATTRIBUTE = 0x40
    DIRECTORY_SYSTEM_ATTRIBUTE = 0x80
    FILE_LAST_WRITE_TIME = 0x100
    DIRECTORY_LAST_WRITE_TIME = 0x200
    PRESERVE_INSYNC_FOR_SYNC_ENGINE = 0x80000000

class StorageProviderPopulationPolicy(enum.IntEnum):
    FULL = 1
    ALWAYS_FULL = 2

class StorageProviderProtectionMode(enum.IntEnum):
    UNKNOWN = 0
    PERSONAL = 1

class StorageProviderState(enum.IntEnum):
    IN_SYNC = 0
    SYNCING = 1
    PAUSED = 2
    ERROR = 3
    WARNING = 4
    OFFLINE = 5

class StorageProviderUriSourceStatus(enum.IntEnum):
    SUCCESS = 0
    NO_SYNC_ROOT = 1
    FILE_NOT_FOUND = 2

class UIStatus(enum.IntEnum):
    UNAVAILABLE = 0
    HIDDEN = 1
    VISIBLE = 2
    COMPLETE = 3

class WriteActivationMode(enum.IntEnum):
    READ_ONLY = 0
    NOT_NEEDED = 1
    AFTER_WRITE = 2

CachedFileUpdater = _ns_module.CachedFileUpdater
CachedFileUpdaterUI = _ns_module.CachedFileUpdaterUI
FileUpdateRequest = _ns_module.FileUpdateRequest
FileUpdateRequestDeferral = _ns_module.FileUpdateRequestDeferral
FileUpdateRequestedEventArgs = _ns_module.FileUpdateRequestedEventArgs
StorageProviderError = _ns_module.StorageProviderError
StorageProviderErrorCommand = _ns_module.StorageProviderErrorCommand
StorageProviderFileTypeInfo = _ns_module.StorageProviderFileTypeInfo
StorageProviderGetContentInfoForPathResult = _ns_module.StorageProviderGetContentInfoForPathResult
StorageProviderGetPathForContentUriResult = _ns_module.StorageProviderGetPathForContentUriResult
StorageProviderItemProperties = _ns_module.StorageProviderItemProperties
StorageProviderItemProperty = _ns_module.StorageProviderItemProperty
StorageProviderItemPropertyDefinition = _ns_module.StorageProviderItemPropertyDefinition
StorageProviderStatus = _ns_module.StorageProviderStatus
StorageProviderSyncRootInfo = _ns_module.StorageProviderSyncRootInfo
StorageProviderSyncRootManager = _ns_module.StorageProviderSyncRootManager
IStorageProviderHandlerFactory = _ns_module.IStorageProviderHandlerFactory
IStorageProviderItemPropertySource = _ns_module.IStorageProviderItemPropertySource
IStorageProviderPropertyCapabilities = _ns_module.IStorageProviderPropertyCapabilities
IStorageProviderStatusSource = _ns_module.IStorageProviderStatusSource
IStorageProviderUriSource = _ns_module.IStorageProviderUriSource
