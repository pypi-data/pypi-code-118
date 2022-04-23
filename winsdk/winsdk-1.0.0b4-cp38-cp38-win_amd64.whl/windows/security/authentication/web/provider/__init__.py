# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Security.Authentication.Web.Provider")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.security.authentication.web
except Exception:
    pass

try:
    import winsdk.windows.security.authentication.web.core
except Exception:
    pass

try:
    import winsdk.windows.security.credentials
except Exception:
    pass

try:
    import winsdk.windows.security.cryptography.core
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

try:
    import winsdk.windows.web.http
except Exception:
    pass

class WebAccountClientViewType(enum.IntEnum):
    ID_ONLY = 0
    ID_AND_PROPERTIES = 1

class WebAccountProviderOperationKind(enum.IntEnum):
    REQUEST_TOKEN = 0
    GET_TOKEN_SILENTLY = 1
    ADD_ACCOUNT = 2
    MANAGE_ACCOUNT = 3
    DELETE_ACCOUNT = 4
    RETRIEVE_COOKIES = 5
    SIGN_OUT_ACCOUNT = 6

class WebAccountScope(enum.IntEnum):
    PER_USER = 0
    PER_APPLICATION = 1

class WebAccountSelectionOptions(enum.IntFlag):
    DEFAULT = 0
    NEW = 0x1

WebAccountClientView = _ns_module.WebAccountClientView
WebAccountManager = _ns_module.WebAccountManager
WebAccountProviderAddAccountOperation = _ns_module.WebAccountProviderAddAccountOperation
WebAccountProviderDeleteAccountOperation = _ns_module.WebAccountProviderDeleteAccountOperation
WebAccountProviderGetTokenSilentOperation = _ns_module.WebAccountProviderGetTokenSilentOperation
WebAccountProviderManageAccountOperation = _ns_module.WebAccountProviderManageAccountOperation
WebAccountProviderRequestTokenOperation = _ns_module.WebAccountProviderRequestTokenOperation
WebAccountProviderRetrieveCookiesOperation = _ns_module.WebAccountProviderRetrieveCookiesOperation
WebAccountProviderSignOutAccountOperation = _ns_module.WebAccountProviderSignOutAccountOperation
WebAccountProviderTriggerDetails = _ns_module.WebAccountProviderTriggerDetails
WebProviderTokenRequest = _ns_module.WebProviderTokenRequest
WebProviderTokenResponse = _ns_module.WebProviderTokenResponse
IWebAccountProviderBaseReportOperation = _ns_module.IWebAccountProviderBaseReportOperation
IWebAccountProviderOperation = _ns_module.IWebAccountProviderOperation
IWebAccountProviderSilentReportOperation = _ns_module.IWebAccountProviderSilentReportOperation
IWebAccountProviderTokenObjects = _ns_module.IWebAccountProviderTokenObjects
IWebAccountProviderTokenObjects2 = _ns_module.IWebAccountProviderTokenObjects2
IWebAccountProviderTokenOperation = _ns_module.IWebAccountProviderTokenOperation
IWebAccountProviderUIReportOperation = _ns_module.IWebAccountProviderUIReportOperation
