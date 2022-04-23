import json
import os
import os.path as Path
import platform
import sys
from hashlib import md5
from importlib.machinery import SourceFileLoader as importer
from logging import Logger
from time import time
from typing import List, Union
from webbrowser import open as FileOpener

import chalk

from .operations import *
from .types import (
    DESTINATION_CHECK_MAP,
    OP_COMMAND,
    OP_COPY,
    OP_CUSTOM,
    OP_DELETE,
    OP_ECHO,
    OP_INPUT,
    OP_INSTRUCTION,
    OP_MOVE,
    OP_REGISTRY,
    OP_REQUEST,
    OP_TASK,
    OP_ZIP,
    OPERATIONS,
    Alias,
    CustomOperation,
    InstructionSet,
    OperationType,
    Settings,
    Task,
)


class Parser:
    def __init__(self, task: str, logger: Logger) -> None:
        self.supported_os = ["Windows"]  # List of Tasker supported OSes
        self.logger = logger
        if task not in self.list_all_tasks():
            self.abort(f"'{task}' InstructionSet was not found")
        self.warn_user()
        self.__first_execution_routine()
        self.task: InstructionSet = json.load(
            open(f"{self.default_location}/{task}.tasker.json", "r")
        )
        analysis = self.__analyse_keys()
        if not analysis[0]:
            self.abort(f'{analysis[3]} "{analysis[1]}" in {analysis[2]}')
        self.__optional_parameters()
        self.settings = self.__get_configs()
        # load extensions
        self.extensions: List[CustomOperation] = self.load_extensions()
        self.__change_relative_locations(self.settings["current_location"])
        self.__executed_tasks: List[Task] = []
        self.__operation_stack: list[OperationType] = []

    def execute(self) -> None:
        self.task["tasks"] = sorted(self.task["tasks"], key=lambda d: d["step"])
        for task in self.task["tasks"]:
            if self.__execute(task):
                self.logger.debug(f"Task \"{task['name']}\" - {chalk.green('OK')}")
            else:
                self.logger.error(f"Task \"{task['name']}\" - {chalk.red('ERROR')}")
        # Reverse Operation Stack
        # Do this to use rollback feature on a reverse order
        self.__operation_stack.reverse()
        tick = True
        for operation in self.__operation_stack:
            if not operation.get_state() and "-No-Rollback" not in os.environ:
                if tick:
                    print()
                    print("--------------  Rollbacks  --------------")
                    print()
                    tick = False
                operation.rollback()

    def warn_user(self) -> None:
        "Verifies if current OS is one of the allowed ones"
        self.system = platform.system()
        if (self.system not in self.supported_os) and ("-No-Warning" not in os.environ):
            ans = input(
                f"'{self.system}' is not part of the current supported OS list.\nAre you sure you want to continue? Y/n\n"
            )
            if ans.lower() == "y":
                pass
            elif ans.lower() == "n":
                sys.exit(0)
            else:
                self.logger.error("Answer not allowed. Aborting...")
                sys.exit(1)

    def abort(self, reason: str) -> None:
        self.logger.error(reason)
        sys.exit(1)

    def __execute(self, task: Task) -> bool:
        try:
            self.__check_destination_path(task, DESTINATION_CHECK_MAP[task["operation"]])
            if task["operation"] == "copy":
                c = Copy(self, task, self.logger)
                self.__operation_stack.append(c)
                c.execute()
            elif task["operation"] == "move":
                m = Move(self, task, self.logger)
                self.__operation_stack.append(m)
                m.execute()
            elif task["operation"] == "delete":
                d = Delete(self, task, self.logger)
                self.__operation_stack.append(d)
                d.execute()
            elif task["operation"] == "zip":
                z = Zip(self, task, self.logger)
                self.__operation_stack.append(z)
                z.execute()
            elif task["operation"] == "command":
                command = Command(self, task, self.logger)
                self.__operation_stack.append(command)
                command.execute()
            elif task["operation"] == "input":
                i = Input(self, task, self.logger)
                self.__operation_stack.append(i)
                i.execute()
            elif task["operation"] == "echo":
                e = Echo(self, task, self.logger)
                self.__operation_stack.append(e)
                e.execute()
            elif task["operation"] == "request":
                r = Request(self, task, self.logger)
                self.__operation_stack.append(r)
                r.execute()
            elif task["operation"] == "registry":
                reg = Registry(self, task, self.logger)
                self.__operation_stack.append(reg)
                reg.execute()
            elif task["operation"] == "custom":
                ex = next(
                    (e for e in self.extensions if e["summon"] == task["extension_name"]),
                    None,
                )
                if ex is None:
                    self.abort(
                        f"No executable found with name {chalk.red(task['extension_name'])}"
                    )
                function: OperationType = ex["executable"].Extension(
                    self, task, self.logger
                )
                self.__operation_stack.append(function)
                function.execute()
            else:
                raise Exception(f"{task['operation']} is an Unknown Operation")
            self.__executed_tasks.append(task)
            return True
        except Exception:
            self.__operation_stack[-1].set_state(False)
            return False

    def __check_destination_path(self, task: Task, needs_path_check: bool = True) -> None:
        "Check destination path if requested end folder is present. If not, create it."
        if needs_path_check:
            if "destination" in task.keys():
                if "$" in task["destination"]:
                    splitted_path = task["destination"].split("/")[-1]
                    if "." in splitted_path:
                        _ = splitted_path.split(".")
                        ref = self._get_step_reference(task, _[0])
                        task["destination"] = ref[_[1]]
                    else:
                        ref = self._get_step_reference(task, task["destination"])
                        task["destination"] = ref["destination"]
            if "origin" in task.keys():
                if "$" in task["origin"]:
                    splitted_path = task["origin"].split("/")[-1]
                    if "." in splitted_path:
                        _ = splitted_path.split(".")
                        ref = self._get_step_reference(task, _[0])
                        task["origin"] = ref[_[1]]
                    else:
                        ref = self._get_step_reference(task, task["destination"])
                        task["destination"] = ref["destination"]
            if "destination" not in task.keys():
                if task["target"].startswith("$"):
                    if "." in task["target"]:
                        _ = task["target"].split(".")
                        ref = self._get_step_reference(task, _[0])
                        task["destination"] = ref[_[1]]
                    else:
                        ref = self._get_step_reference(task, task["target"])
                        task["destination"] = ref["destination"]
                else:
                    self.logger.debug("Destination parameter is not present")
                    raise Exception()
            destination = task["destination"].split("/")[-1]
            destination_parent = "/".join(_ for _ in task["destination"].split("/")[:-1])
            if destination not in os.listdir(f"{destination_parent}"):
                os.mkdir(f"{task['destination']}")

    def __analyse_keys(
        self,
    ) -> tuple[bool, Union[str, None], Union[str, None], Union[str, None]]:
        "Verify if the structure of the Instruction Set is defined correctly"
        for key in OP_INSTRUCTION:
            if key not in self.task.keys():
                return (False, key, "Definition", "Missing key")
        if len(self.task["tasks"]) > 0:
            for _task in self.task["tasks"]:
                for key in OP_TASK:
                    if key not in _task.keys():
                        return (False, key, "Task", "Missing key")
                op = _task["operation"]
                if op not in OPERATIONS:
                    return (False, op, f"\"{_task['name']}\" Task", "Unknown Operation")
                operation_keys: list[str] = eval(f"OP_{op.upper()}")
                for key in operation_keys:
                    if key not in _task.keys():
                        # Check for optional parameters
                        if not key.startswith("!"):
                            return (
                                False,
                                key,
                                f"\"{_task['name']}\" Task",
                                "Missing key",
                            )
        return (True, None, None, None)

    def __optional_parameters(self) -> None:
        to_change = []
        for i in range(len(self.task["tasks"])):
            # Replace optional parameter identifier with a definitive one
            for key in self.task["tasks"][i].keys():
                if key.startswith("!"):
                    to_change.append([i, key])
        for obj in to_change:
            self.task["tasks"][obj[0]][obj[1].replace("!", "")] = self.task["tasks"][
                obj[0]
            ][obj[1]]
            del self.task["tasks"][obj[0]][obj[1]]

    def _get_all_file_paths(self, directory: str) -> List[str]:
        file_paths = []
        for root, _, files in os.walk(directory):
            for filename in files:
                file_paths.append(Path.join(root, filename).replace("\\", "/"))
        return file_paths

    def __change_relative_locations(self, home: str) -> None:
        for task in self.task["tasks"]:
            if home != None or home != "":
                if "destination" in task.keys():
                    task["destination"] = f"{home}/{task['destination']}".replace(
                        "\\", "/"
                    )
                if "origin" in task.keys() and ":" not in task["origin"]:
                    task["origin"] = f"{home}/{task['origin']}".replace("\\", "/")

    def _get_step_reference(self, task: Task, ref: str) -> Union[Task, dict]:
        # get step in reference
        step_index = next(
            (
                index
                for (index, d) in enumerate(self.__executed_tasks)
                if d["step"] == int(ref.replace("$", ""))
            ),
            None,
        )
        if step_index == None:
            self.logger.error(
                f"Reference in Task \"{task['name']}\" is either not been executed or doesn't exist."
            )
            raise Exception()
        vars = {}
        for _ in self.__operation_stack:
            if _.task["step"] == step_index:
                vars = _.__dict__
                break
        return dict(self.__executed_tasks[step_index], **vars)

    def __first_execution_routine(self) -> None:
        "Create the initial configuration and setup necessary directories"
        self.do_config()
        root_path = Path.expanduser("~")
        self.default_location = f"{root_path}/.tasker/Tasks"
        # TODO: validate entry point for Starting Location on config file

    def __get_configs(self) -> Settings:
        j: Settings = json.load(open(f"{Path.expanduser('~')}/.tasker/config.json"))
        return j

    def load_extensions(self) -> List[CustomOperation]:
        modules: List[CustomOperation] = []
        for extension in self.settings["extensions"]:
            # sys.path.insert(0, extension["path"])
            spec: OperationType = importer(f"{extension['file'].replace('.py', '')}", extension["path"]).load_module()  # type: ignore
            modules.append({"executable": spec, "summon": extension["name"]})
        return modules

    # Static Methods

    @staticmethod
    def do_config() -> None:
        "Create the initial configuration and setup necessary directories"

        def create_initial_config(p: str) -> None:
            with open(f"{p}/.tasker/config.json", "w") as config:
                json.dump(
                    {
                        "current_location": p,
                        "default_location": p,
                        "extensions": [],
                        "alias": [],
                    },
                    config,
                    indent=4,
                )
                config.close()
            with open(f"{p}/.tasker/template.txt", "w") as template:
                template.write(
                    """\
from logging import Logger

from Tasker.inspector import implements

from Tasker.types import OperationType as Operation
from Tasker.types import Task
from Tasker.types import ParserType as Parser


@implements(Operation)
class Extension:
    "<name> Action"

    __annotations__ = {
        "name": "<name> Action",
        "intent": "<description>",
    }

    def __init__(self, ctx: Parser, task: Task, logger: Logger) -> None:
        self.context = ctx  # Parser Context
        self.task = task  # Current assigned Task
        self.logger = logger
        self.affected_files: list[str] = []
        self.__internal_state = True  # Faulty execution flag
        self._type = "Custom"
        self.handle_references()

    def execute(self) -> None:
        # Execution Block
        pass

    def rollback(self) -> None:
        # Rollback Block
        pass

    def set_state(self, state: bool) -> None:
        "Sets the state for the Internal Fault flag"
        self.__internal_state = state

    def get_state(self) -> bool:
        "Returns the of the Internal Fault flag"
        return self.__internal_state

    def handle_references(self) -> None:
        for key in self.task.keys():
            if type(self.task[key]) == str and self.task[key].startswith("$"):
                if "." in self.task[key]:
                    _ = self.task[key].split(".")
                    step = self.context._get_step_reference(self.task, _[0])
                    self.task[key] = step[_[1]]
                else:
                    step = self.context._get_step_reference(self.task, self.task[key])
                    self.task[key] = step[key]"""
                )

        root_path = Path.expanduser("~")
        root_folders = os.listdir(root_path)
        if ".tasker" not in root_folders:
            os.mkdir(f"{root_path}/.tasker")
            os.mkdir(f"{root_path}/.tasker/Tasks")
            os.mkdir(f"{root_path}/.tasker/Templates")
            create_initial_config(root_path)
        else:
            tasker_folder = os.listdir(f"{root_path}/.tasker")
            if "Tasks" not in tasker_folder:
                os.mkdir(f"{root_path}/.tasker/Tasks")

            if "Templates" not in tasker_folder:
                os.mkdir(f"{root_path}/.tasker/Templates")

            if ("config.json" not in tasker_folder) or (
                "template.txt" not in tasker_folder
            ):
                create_initial_config(root_path)

    @staticmethod
    def list_all_tasks() -> List[str]:
        "Lists all Task templates created"
        Parser.do_config()
        return [
            _.replace(".tasker.json", "")
            for _ in os.listdir(f"{Path.expanduser('~')}/.tasker/Tasks")
        ]

    @staticmethod
    def create_new_task(file_name: str, name: str, description: str) -> InstructionSet:
        Parser.do_config()
        i: InstructionSet = {"name": name, "description": description, "tasks": []}
        with open(
            f"{Path.expanduser('~')}/.tasker/Tasks/{file_name}.tasker.json", "w"
        ) as instruction_set:
            json.dump(i, instruction_set, indent=4)
            instruction_set.close()
        return i

    @staticmethod
    def open_file_for_edit(file: str) -> None:
        Parser.do_config()
        FileOpener(f"{Path.expanduser('~')}/.tasker/Tasks/{file}.tasker.json")

    @staticmethod
    def create_extension(name: str) -> None:
        Parser.do_config()
        root = Path.expanduser("~")
        with open(f"{root}/.tasker/template.txt", "r") as template:
            t = template.read()
            t = t.replace("<name>", name)
            _n = md5(f"{time()}_{name}".encode("UTF-8")).hexdigest()[:10]
            f_name = f"extension_{_n}.py"
            with open(f"{root}/.tasker/Templates/{f_name}", "w") as ex:
                ex.write(t)
                ex.close()
            j: Settings = json.load(open(f"{root}/.tasker/config.json"))
            j["extensions"].append(
                {
                    "name": name,
                    "file": f_name,
                    "path": f"{root}/.tasker/Templates/{f_name}",
                }
            )
            json.dump(j, open(f"{root}/.tasker/config.json", "w"), indent=4)
            template.close()

    @staticmethod
    def add_alias(alias: Alias, logger: Logger) -> None:
        root = Path.expanduser("~")
        settings: Settings = json.load(open(f"{root}/.tasker/config.json"))
        # check if alias is already present
        for _alias in settings["alias"]:
            if alias["name"] == _alias["name"]:
                logger.error("An Alias with that name already exists")
                sys.exit(1)
        settings["alias"].append(alias)
        json.dump(settings, open(f"{root}/.tasker/config.json", "w"), indent=4)
