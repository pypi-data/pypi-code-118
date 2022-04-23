# SPDX-License-Identifier: MIT OR Apache-2.0
# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the MIT License.  See the LICENSE file in the root of this
# repository for complete details.

"""
Extracted log level data used by both stdlib and native log level filters.
"""

from typing import Any, Callable, Type

from structlog._base import BoundLoggerBase
from structlog.types import FilteringBoundLogger

# Adapted from the stdlib
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
TRACE = 5
NOTSET = 0

_NAME_TO_LEVEL = {
    "critical": CRITICAL,
    "exception": ERROR,
    "error": ERROR,
    "warn": WARNING,
    "warning": WARNING,
    "info": INFO,
    "debug": DEBUG,
    "trace": TRACE,
    "notset": NOTSET,
}

_LEVEL_TO_NAME = {
    v: k for k, v in _NAME_TO_LEVEL.items() if k not in ("warn", "exception", "notset")
}


def _nop(*args: Any, **kw: Any) -> Any:
    return None


def exception(self: FilteringBoundLogger, event: str, **kw: Any) -> Any:
    kw.setdefault("exc_info", True)

    return self.error(event, **kw)


def msg(self: FilteringBoundLogger, event: str, **kw: Any) -> Any:
    level = kw.get("level", INFO)
    if level >= INFO:
        return self.info(event, **kw)
    else:
        return self.debug(event, **kw)


def make_filtering_bound_logger(min_level: int) -> Type[FilteringBoundLogger]:
    """
    Create a new `FilteringBoundLogger` that only logs *min_level* or higher.

    The logger is optimized such that log levels below *min_level* only consist
    of a ``return None``.

    Compared to using ``structlog``'s standard library integration and the
    `structlog.stdlib.filter_by_level` processor:

    - It's faster because once the logger is built at program start, it's a
      static class.
    - For the same reason you can't change the log level once configured.
      Use the dynamic approach of `standard-library` instead, if you need this
      feature.

    :param min_level: The log level as an integer. You can use the constants
        from `logging` like ``logging.INFO`` or pass the values directly. See
        `this table from the logging docs
        <https://docs.python.org/3/library/logging.html#levels>`_ for possible
        values.

    .. versionadded:: 20.2.0
    .. versionchanged:: 21.1.0 The returned loggers are now pickleable.
    """

    return _LEVEL_TO_FILTERING_LOGGER[min_level]


def _make_filtering_bound_logger(min_level: int) -> Type[FilteringBoundLogger]:
    """
    Create a new `FilteringBoundLogger` that only logs *min_level* or higher.

    The logger is optimized such that log levels below *min_level* only consist
    of a ``return None``.
    """

    def make_method(level: int) -> Callable[..., Any]:
        if level < min_level:
            return _nop

        name = _LEVEL_TO_NAME[level]

        def meth(self: Any, event: str, **kw: Any) -> Any:
            return self._proxy_to_logger(name, event, **kw)

        meth.__name__ = name

        return meth

    meths = {}
    for lvl, name in _LEVEL_TO_NAME.items():
        meths[name] = make_method(lvl)

    meths["exception"] = exception
    meths["fatal"] = meths["error"]
    meths["warn"] = meths["warning"]
    meths["msg"] = msg
    meths["trace"] = meths["debug"]

    return type(
        "BoundLoggerFilteringAt%s"
        % (_LEVEL_TO_NAME.get(min_level, "Notset").capitalize()),
        (BoundLoggerBase,),
        meths,
    )


# Pre-create all possible filters to make them pickleable.
BoundLoggerFilteringAtNotset = _make_filtering_bound_logger(NOTSET)
BoundLoggerFilteringAtTrace = _make_filtering_bound_logger(5)
BoundLoggerFilteringAtDebug = _make_filtering_bound_logger(DEBUG)
BoundLoggerFilteringAtInfo = _make_filtering_bound_logger(INFO)
BoundLoggerFilteringAtWarning = _make_filtering_bound_logger(WARNING)
BoundLoggerFilteringAtError = _make_filtering_bound_logger(ERROR)
BoundLoggerFilteringAtCritical = _make_filtering_bound_logger(CRITICAL)

_LEVEL_TO_FILTERING_LOGGER = {
    CRITICAL: BoundLoggerFilteringAtCritical,
    ERROR: BoundLoggerFilteringAtError,
    WARNING: BoundLoggerFilteringAtWarning,
    INFO: BoundLoggerFilteringAtInfo,
    DEBUG: BoundLoggerFilteringAtDebug,
    TRACE: BoundLoggerFilteringAtTrace,
    NOTSET: BoundLoggerFilteringAtNotset,
}
