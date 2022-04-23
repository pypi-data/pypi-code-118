# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Globalization.PhoneNumberFormatting")

class PhoneNumberFormat(enum.IntEnum):
    E164 = 0
    INTERNATIONAL = 1
    NATIONAL = 2
    RFC3966 = 3

class PhoneNumberMatchResult(enum.IntEnum):
    NO_MATCH = 0
    SHORT_NATIONAL_SIGNIFICANT_NUMBER_MATCH = 1
    NATIONAL_SIGNIFICANT_NUMBER_MATCH = 2
    EXACT_MATCH = 3

class PhoneNumberParseResult(enum.IntEnum):
    VALID = 0
    NOT_A_NUMBER = 1
    INVALID_COUNTRY_CODE = 2
    TOO_SHORT = 3
    TOO_LONG = 4

class PredictedPhoneNumberKind(enum.IntEnum):
    FIXED_LINE = 0
    MOBILE = 1
    FIXED_LINE_OR_MOBILE = 2
    TOLL_FREE = 3
    PREMIUM_RATE = 4
    SHARED_COST = 5
    VOIP = 6
    PERSONAL_NUMBER = 7
    PAGER = 8
    UNIVERSAL_ACCOUNT_NUMBER = 9
    VOICEMAIL = 10
    UNKNOWN = 11

PhoneNumberFormatter = _ns_module.PhoneNumberFormatter
PhoneNumberInfo = _ns_module.PhoneNumberInfo
