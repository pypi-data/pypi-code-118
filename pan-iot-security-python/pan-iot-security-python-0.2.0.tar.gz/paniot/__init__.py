#
# Copyright (c) 2022 Palo Alto Networks, Inc.
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

import asyncio
from collections import namedtuple
import logging
import re
import sys

__version__ = '0.2.0'

_default_api_version = (4, 0)
DEFAULT_API_VERSION = 'v%d.%d' % _default_api_version

DEBUG1 = logging.DEBUG
DEBUG2 = DEBUG1 - 1
DEBUG3 = DEBUG2 - 1

logging.addLevelName(DEBUG2, 'DEBUG2')
logging.addLevelName(DEBUG3, 'DEBUG3')


class ApiError(Exception):
    pass


class ArgsError(ApiError):
    pass


class ApiVersion(namedtuple('api_version',
                            ['major', 'minor'])):
    def __str__(self):
        return 'v%d.%d' % (self.major, self.minor)

    def __int__(self):
        # reserve lower 8 bits for 'future' use
        return self.major << 16 | self.minor << 8


def _isaio():
    try:
        asyncio.get_running_loop()
        return True
    except RuntimeError:
        return False


def IotApi(api_version=None, *args, **kwargs):
    _log = logging.getLogger(__name__).log

    if api_version is None:
        x = _default_api_version
    else:
        r = re.search(r'^v?(\d+)\.(\d+)$', api_version)
        if r is None:
            raise ArgsError('Invalid api_version: %s' % api_version)
        x = int(r.group(1)), int(r.group(2))
    _api_version = ApiVersion(*x)
    _log(DEBUG1, 'api_version: %s, 0x%06x',
         _api_version, int(_api_version))

    package = 'paniot'
    name = 'aioapi' if _isaio() else 'api'
    module = 'v%d_%d%s' % (_api_version.major,
                           _api_version.minor,
                           name)
    module_name = '%s.%s' % (package, module)
    class_ = 'IotApi'

    try:
        __import__(module_name)
    except ImportError as e:
        raise ArgsError('Module import error: %s: %s' %
                        (module_name, e))

    try:
        klass = getattr(sys.modules[module_name], class_)
    except AttributeError:
        raise ArgsError('Class not found: %s' % class_)

    return klass(api_version=_api_version, *args, **kwargs)
