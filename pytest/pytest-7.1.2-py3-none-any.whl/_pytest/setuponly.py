from typing import Generator
from typing import Optional
from typing import Union

import pytest
from _pytest._io.saferepr import saferepr
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureDef
from _pytest.fixtures import SubRequest
from _pytest.scope import Scope


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup("debugconfig")
    group.addoption(
        "--setuponly",
        "--setup-only",
        action="store_true",
        help="only setup fixtures, do not execute tests.",
    )
    group.addoption(
        "--setupshow",
        "--setup-show",
        action="store_true",
        help="show setup of fixtures while executing tests.",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(
    fixturedef: FixtureDef[object], request: SubRequest
) -> Generator[None, None, None]:
    yield
    if request.config.option.setupshow:
        if hasattr(request, "param"):
            # Save the fixture parameter so ._show_fixture_action() can
            # display it now and during the teardown (in .finish()).
            if fixturedef.ids:
                if callable(fixturedef.ids):
                    param = fixturedef.ids(request.param)
                else:
                    param = fixturedef.ids[request.param_index]
            else:
                param = request.param
            fixturedef.cached_param = param  # type: ignore[attr-defined]
        _show_fixture_action(fixturedef, "SETUP")


def pytest_fixture_post_finalizer(fixturedef: FixtureDef[object]) -> None:
    if fixturedef.cached_result is not None:
        config = fixturedef._fixturemanager.config
        if config.option.setupshow:
            _show_fixture_action(fixturedef, "TEARDOWN")
            if hasattr(fixturedef, "cached_param"):
                del fixturedef.cached_param  # type: ignore[attr-defined]


def _show_fixture_action(fixturedef: FixtureDef[object], msg: str) -> None:
    config = fixturedef._fixturemanager.config
    capman = config.pluginmanager.getplugin("capturemanager")
    if capman:
        capman.suspend_global_capture()

    tw = config.get_terminal_writer()
    tw.line()
    # Use smaller indentation the higher the scope: Session = 0, Package = 1, etc.
    scope_indent = list(reversed(Scope)).index(fixturedef._scope)
    tw.write(" " * 2 * scope_indent)
    tw.write(
        "{step} {scope} {fixture}".format(
            step=msg.ljust(8),  # align the output to TEARDOWN
            scope=fixturedef.scope[0].upper(),
            fixture=fixturedef.argname,
        )
    )

    if msg == "SETUP":
        deps = sorted(arg for arg in fixturedef.argnames if arg != "request")
        if deps:
            tw.write(" (fixtures used: {})".format(", ".join(deps)))

    if hasattr(fixturedef, "cached_param"):
        tw.write(f"[{saferepr(fixturedef.cached_param, maxsize=42)}]")  # type: ignore[attr-defined]

    tw.flush()

    if capman:
        capman.resume_global_capture()


@pytest.hookimpl(tryfirst=True)
def pytest_cmdline_main(config: Config) -> Optional[Union[int, ExitCode]]:
    if config.option.setuponly:
        config.option.setupshow = True
    return None
