# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.4

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Security.Cryptography")

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class BinaryStringEncoding(enum.IntEnum):
    UTF8 = 0
    UTF16_L_E = 1
    UTF16_B_E = 2

CryptographicBuffer = _ns_module.CryptographicBuffer
