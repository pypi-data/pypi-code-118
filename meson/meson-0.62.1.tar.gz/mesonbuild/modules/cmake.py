# Copyright 2018 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
import re
import os, os.path, pathlib
import shutil
import typing as T

from . import ExtensionModule, ModuleReturnValue, ModuleObject

from .. import build, mesonlib, mlog, dependencies
from ..cmake import SingleTargetOptions, TargetOptions, cmake_defines_to_args
from ..interpreter import SubprojectHolder
from ..interpreter.type_checking import REQUIRED_KW, NoneType, in_set_validator
from ..interpreterbase import (
    FeatureNew,
    FeatureNewKwargs,

    stringArgs,
    permittedKwargs,
    noPosargs,
    noKwargs,

    InvalidArguments,
    InterpreterException,

    typed_pos_args,
    typed_kwargs,
    KwargInfo,
    ContainerTypeInfo,
)

if T.TYPE_CHECKING:
    from typing_extensions import TypedDict

    from . import ModuleState
    from ..interpreter import kwargs

    class WriteBasicPackageVersionFile(TypedDict):

        arch_independent: bool
        compatibility: str
        install_dir: T.Optional[str]
        name: str
        version: str

    class ConfigurePackageConfigFile(TypedDict):

        configuration: T.Union[build.ConfigurationData, dict]
        input: T.Union[str, mesonlib.File]
        install_dir: T.Optional[str]
        name: str

    class Subproject(kwargs.ExtractRequired):

        options: T.Optional[CMakeSubprojectOptions]
        cmake_options: T.List[str]


COMPATIBILITIES = ['AnyNewerVersion', 'SameMajorVersion', 'SameMinorVersion', 'ExactVersion']

# Taken from https://github.com/Kitware/CMake/blob/master/Modules/CMakePackageConfigHelpers.cmake
PACKAGE_INIT_BASE = '''
####### Expanded from \\@PACKAGE_INIT\\@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was @inputFileName@ ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/@PACKAGE_RELATIVE_PATH@" ABSOLUTE)
'''
PACKAGE_INIT_EXT = '''
# Use original install prefix when loaded through a "/usr move"
# cross-prefix symbolic link such as /lib -> /usr/lib.
get_filename_component(_realCurr "${CMAKE_CURRENT_LIST_DIR}" REALPATH)
get_filename_component(_realOrig "@absInstallDir@" REALPATH)
if(_realCurr STREQUAL _realOrig)
  set(PACKAGE_PREFIX_DIR "@installPrefix@")
endif()
unset(_realOrig)
unset(_realCurr)
'''
PACKAGE_INIT_SET_AND_CHECK = '''
macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

####################################################################################
'''

class CMakeSubproject(ModuleObject):
    def __init__(self, subp: SubprojectHolder):
        assert isinstance(subp, SubprojectHolder)
        assert subp.cm_interpreter is not None
        super().__init__()
        self.subp = subp
        self.cm_interpreter = subp.cm_interpreter
        self.methods.update({'get_variable': self.get_variable,
                             'dependency': self.dependency,
                             'include_directories': self.include_directories,
                             'target': self.target,
                             'target_type': self.target_type,
                             'target_list': self.target_list,
                             'found': self.found_method,
                             })

    def _args_to_info(self, args):
        if len(args) != 1:
            raise InterpreterException('Exactly one argument is required.')

        tgt = args[0]
        res = self.cm_interpreter.target_info(tgt)
        if res is None:
            raise InterpreterException(f'The CMake target {tgt} does not exist\n' +
                                       '  Use the following command in your meson.build to list all available targets:\n\n' +
                                       '    message(\'CMaket targets:\\n - \' + \'\\n - \'.join(<cmake_subproject>.target_list()))')

        # Make sure that all keys are present (if not this is a bug)
        assert all([x in res for x in ['inc', 'src', 'dep', 'tgt', 'func']])
        return res

    @noKwargs
    @stringArgs
    def get_variable(self, state, args, kwargs):
        return self.subp.get_variable_method(args, kwargs)

    @FeatureNewKwargs('dependency', '0.56.0', ['include_type'])
    @permittedKwargs({'include_type'})
    @stringArgs
    def dependency(self, state, args, kwargs):
        info = self._args_to_info(args)
        if info['func'] == 'executable':
            raise InvalidArguments(f'{args[0]} is an executable and does not support the dependency() method. Use target() instead.')
        orig = self.get_variable(state, [info['dep']], {})
        assert isinstance(orig, dependencies.Dependency)
        actual = orig.include_type
        if 'include_type' in kwargs and kwargs['include_type'] != actual:
            mlog.debug('Current include type is {}. Converting to requested {}'.format(actual, kwargs['include_type']))
            return orig.generate_system_dependency(kwargs['include_type'])
        return orig

    @noKwargs
    @stringArgs
    def include_directories(self, state, args, kwargs):
        info = self._args_to_info(args)
        return self.get_variable(state, [info['inc']], kwargs)

    @noKwargs
    @stringArgs
    def target(self, state, args, kwargs):
        info = self._args_to_info(args)
        return self.get_variable(state, [info['tgt']], kwargs)

    @noKwargs
    @stringArgs
    def target_type(self, state, args, kwargs):
        info = self._args_to_info(args)
        return info['func']

    @noPosargs
    @noKwargs
    def target_list(self, state, args, kwargs):
        return self.cm_interpreter.target_list()

    @noPosargs
    @noKwargs
    @FeatureNew('CMakeSubproject.found()', '0.53.2')
    def found_method(self, state, args, kwargs):
        return self.subp is not None


class CMakeSubprojectOptions(ModuleObject):
    def __init__(self) -> None:
        super().__init__()
        self.cmake_options = []  # type: T.List[str]
        self.target_options = TargetOptions()

        self.methods.update(
            {
                'add_cmake_defines': self.add_cmake_defines,
                'set_override_option': self.set_override_option,
                'set_install': self.set_install,
                'append_compile_args': self.append_compile_args,
                'append_link_args': self.append_link_args,
                'clear': self.clear,
            }
        )

    def _get_opts(self, kwargs: dict) -> SingleTargetOptions:
        if 'target' in kwargs:
            return self.target_options[kwargs['target']]
        return self.target_options.global_options

    @noKwargs
    def add_cmake_defines(self, state, args, kwargs) -> None:
        self.cmake_options += cmake_defines_to_args(args)

    @stringArgs
    @permittedKwargs({'target'})
    def set_override_option(self, state, args, kwargs) -> None:
        if len(args) != 2:
            raise InvalidArguments('set_override_option takes exactly 2 positional arguments')
        self._get_opts(kwargs).set_opt(args[0], args[1])

    @permittedKwargs({'target'})
    def set_install(self, state, args, kwargs) -> None:
        if len(args) != 1 or not isinstance(args[0], bool):
            raise InvalidArguments('set_install takes exactly 1 boolean argument')
        self._get_opts(kwargs).set_install(args[0])

    @stringArgs
    @permittedKwargs({'target'})
    def append_compile_args(self, state, args, kwargs) -> None:
        if len(args) < 2:
            raise InvalidArguments('append_compile_args takes at least 2 positional arguments')
        self._get_opts(kwargs).append_args(args[0], args[1:])

    @stringArgs
    @permittedKwargs({'target'})
    def append_link_args(self, state, args, kwargs) -> None:
        if not args:
            raise InvalidArguments('append_link_args takes at least 1 positional argument')
        self._get_opts(kwargs).append_link_args(args)

    @noPosargs
    @noKwargs
    def clear(self, state, args, kwargs) -> None:
        self.cmake_options.clear()
        self.target_options = TargetOptions()


class CmakeModule(ExtensionModule):
    cmake_detected = False
    cmake_root = None

    @FeatureNew('CMake Module', '0.50.0')
    def __init__(self, interpreter):
        super().__init__(interpreter)
        self.methods.update({
            'write_basic_package_version_file': self.write_basic_package_version_file,
            'configure_package_config_file': self.configure_package_config_file,
            'subproject': self.subproject,
            'subproject_options': self.subproject_options,
        })

    def detect_voidp_size(self, env):
        compilers = env.coredata.compilers.host
        compiler = compilers.get('c', None)
        if not compiler:
            compiler = compilers.get('cpp', None)

        if not compiler:
            raise mesonlib.MesonException('Requires a C or C++ compiler to compute sizeof(void *).')

        return compiler.sizeof('void *', '', env)

    def detect_cmake(self, state):
        if self.cmake_detected:
            return True

        cmakebin = state.find_program('cmake', silent=False)
        if not cmakebin.found():
            return False

        p, stdout, stderr = mesonlib.Popen_safe(cmakebin.get_command() + ['--system-information', '-G', 'Ninja'])[0:3]
        if p.returncode != 0:
            mlog.log(f'error retrieving cmake information: returnCode={p.returncode} stdout={stdout} stderr={stderr}')
            return False

        match = re.search('\nCMAKE_ROOT \\"([^"]+)"\n', stdout.strip())
        if not match:
            mlog.log('unable to determine cmake root')
            return False

        cmakePath = pathlib.PurePath(match.group(1))
        self.cmake_root = os.path.join(*cmakePath.parts)
        self.cmake_detected = True
        return True

    @noPosargs
    @typed_kwargs(
        'cmake.write_basic_package_version_file',
        KwargInfo('arch_independent', bool, default=False, since='0.62.0'),
        KwargInfo('compatibility', str, default='AnyNewerVersion', validator=in_set_validator(set(COMPATIBILITIES))),
        KwargInfo('install_dir', (str, NoneType), default=None),
        KwargInfo('name', str, required=True),
        KwargInfo('version', str, required=True),
    )
    def write_basic_package_version_file(self, state, args, kwargs: 'WriteBasicPackageVersionFile'):
        arch_independent = kwargs['arch_independent']
        compatibility = kwargs['compatibility']
        name = kwargs['name']
        version = kwargs['version']

        if not self.detect_cmake(state):
            raise mesonlib.MesonException('Unable to find cmake')

        pkgroot = pkgroot_name = kwargs['install_dir']
        if pkgroot is None:
            pkgroot = os.path.join(state.environment.coredata.get_option(mesonlib.OptionKey('libdir')), 'cmake', name)
            pkgroot_name = os.path.join('{libdir}', 'cmake', name)

        template_file = os.path.join(self.cmake_root, 'Modules', f'BasicConfigVersion-{compatibility}.cmake.in')
        if not os.path.exists(template_file):
            raise mesonlib.MesonException(f'your cmake installation doesn\'t support the {compatibility} compatibility')

        version_file = os.path.join(state.environment.scratch_dir, f'{name}ConfigVersion.cmake')

        conf = {
            'CVF_VERSION': (version, ''),
            'CMAKE_SIZEOF_VOID_P': (str(self.detect_voidp_size(state.environment)), ''),
            'CVF_ARCH_INDEPENDENT': (arch_independent, ''),
        }
        mesonlib.do_conf_file(template_file, version_file, conf, 'meson')

        res = build.Data([mesonlib.File(True, state.environment.get_scratch_dir(), version_file)], pkgroot, pkgroot_name, None, state.subproject)
        return ModuleReturnValue(res, [res])

    def create_package_file(self, infile, outfile, PACKAGE_RELATIVE_PATH, extra, confdata):
        package_init = PACKAGE_INIT_BASE.replace('@PACKAGE_RELATIVE_PATH@', PACKAGE_RELATIVE_PATH)
        package_init = package_init.replace('@inputFileName@', os.path.basename(infile))
        package_init += extra
        package_init += PACKAGE_INIT_SET_AND_CHECK

        try:
            with open(infile, encoding='utf-8') as fin:
                data = fin.readlines()
        except Exception as e:
            raise mesonlib.MesonException(f'Could not read input file {infile}: {e!s}')

        result = []
        regex = mesonlib.get_variable_regex('cmake@')
        for line in data:
            line = line.replace('@PACKAGE_INIT@', package_init)
            line, _missing = mesonlib.do_replacement(regex, line, 'cmake@', confdata)

            result.append(line)

        outfile_tmp = outfile + "~"
        with open(outfile_tmp, "w", encoding='utf-8') as fout:
            fout.writelines(result)

        shutil.copymode(infile, outfile_tmp)
        mesonlib.replace_if_different(outfile, outfile_tmp)

    @noPosargs
    @typed_kwargs(
        'cmake.configure_package_config_file',
        KwargInfo('configuration', (build.ConfigurationData, dict), required=True),
        KwargInfo('input',
                  (str, mesonlib.File, ContainerTypeInfo(list, mesonlib.File)), required=True,
                  validator=lambda x: 'requires exactly one file' if isinstance(x, list) and len(x) != 1 else None,
                  convertor=lambda x: x[0] if isinstance(x, list) else x),
        KwargInfo('install_dir', (str, NoneType), default=None),
        KwargInfo('name', str, required=True),
    )
    def configure_package_config_file(self, state, args, kwargs: 'ConfigurePackageConfigFile'):
        inputfile = kwargs['input']
        if isinstance(inputfile, str):
            inputfile = mesonlib.File.from_source_file(state.environment.source_dir, state.subdir, inputfile)

        ifile_abs = inputfile.absolute_path(state.environment.source_dir, state.environment.build_dir)

        name = kwargs['name']

        (ofile_path, ofile_fname) = os.path.split(os.path.join(state.subdir, f'{name}Config.cmake'))
        ofile_abs = os.path.join(state.environment.build_dir, ofile_path, ofile_fname)

        install_dir = kwargs['install_dir']
        if install_dir is None:
            install_dir = os.path.join(state.environment.coredata.get_option(mesonlib.OptionKey('libdir')), 'cmake', name)

        conf = kwargs['configuration']
        if isinstance(conf, dict):
            FeatureNew.single_use('cmake.configure_package_config_file dict as configuration', '0.62.0', state.subproject, location=state.current_node)
            conf = build.ConfigurationData(conf)

        prefix = state.environment.coredata.get_option(mesonlib.OptionKey('prefix'))
        abs_install_dir = install_dir
        if not os.path.isabs(abs_install_dir):
            abs_install_dir = os.path.join(prefix, install_dir)

        PACKAGE_RELATIVE_PATH = os.path.relpath(prefix, abs_install_dir)
        extra = ''
        if re.match('^(/usr)?/lib(64)?/.+', abs_install_dir):
            extra = PACKAGE_INIT_EXT.replace('@absInstallDir@', abs_install_dir)
            extra = extra.replace('@installPrefix@', prefix)

        self.create_package_file(ifile_abs, ofile_abs, PACKAGE_RELATIVE_PATH, extra, conf)
        conf.used = True

        conffile = os.path.normpath(inputfile.relative_name())
        self.interpreter.build_def_files.add(conffile)

        res = build.Data([mesonlib.File(True, ofile_path, ofile_fname)], install_dir, install_dir, None, state.subproject)
        self.interpreter.build.data.append(res)

        return res

    @FeatureNew('subproject', '0.51.0')
    @typed_pos_args('cmake.subproject', str)
    @typed_kwargs(
        'cmake.subproject',
        REQUIRED_KW,
        KwargInfo('options', (CMakeSubprojectOptions, NoneType), since='0.55.0'),
        KwargInfo(
            'cmake_options',
            ContainerTypeInfo(list, str),
            default=[],
            listify=True,
            deprecated='0.55.0',
            deprecated_message='Use options instead',
        ),
    )
    def subproject(self, state: ModuleState, args: T.Tuple[str], kwargs_: Subproject) -> T.Union[SubprojectHolder, CMakeSubproject]:
        if kwargs_['cmake_options'] and kwargs_['options'] is not None:
            raise InterpreterException('"options" cannot be used together with "cmake_options"')
        dirname = args[0]
        kw: kwargs.DoSubproject = {
            'required': kwargs_['required'],
            'options': kwargs_['options'],
            'cmake_options': kwargs_['cmake_options'],
            'default_options': [],
            'version': [],
        }
        subp = self.interpreter.do_subproject(dirname, 'cmake', kw)
        if not subp.found():
            return subp
        return CMakeSubproject(subp)

    @FeatureNew('subproject_options', '0.55.0')
    @noKwargs
    @noPosargs
    def subproject_options(self, state, args, kwargs) -> CMakeSubprojectOptions:
        return CMakeSubprojectOptions()

def initialize(*args, **kwargs):
    return CmakeModule(*args, **kwargs)
