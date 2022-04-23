from pathlib import Path
import itertools
import subprocess
import typing
import enum


class Status(enum.Enum):
    SEEN = ' '
    FLAGGED = '*'
    UNSEEN = '.'
    TRASHED = 'x'
    VIRTUAL = 'v'


class Directory(typing.NamedTuple):
    path: typing.Optional[str]
    name: str
    children: typing.List['Directory']


class Message(typing.NamedTuple):
    path: str
    status: Status
    subject: str
    sender: str
    date: str
    children: typing.List['Message']


def get_directories(roots: typing.Iterable[str]) -> typing.List[Directory]:
    paths = _cmd(['mdirs', '-a', *roots])
    directories = (_get_directory(path, Path(path).parts) for path in paths)
    directories = _group_directories(directories)
    directories = [_reduce_directory(directory) for directory in directories]
    return directories


def get_directory_total(dir_path: str) -> int:
    paths = _cmd(['mlist', dir_path])
    return len(paths)


def get_directory_unseen(dir_path: str) -> int:
    paths = _cmd(['mlist', '-s', dir_path])
    return len(paths)


def get_messages(dir_path: str) -> typing.List[Message]:
    paths = _cmd(['mlist', dir_path])
    paths = _cmd(['mthread', '-r'], paths)
    lines = _cmd(['mscan', '-f', r'%i%R\n%u\n%s\n%f\n%D'], paths)
    messages = _parse_messages(lines)
    return messages


def get_message(msg_path: str) -> str:
    if not Path(msg_path).exists():
        return ''
    lines = _cmd(['mshow', msg_path])
    return '\n'.join(lines)


def _cmd(args, stdin_lines=[]):
    p = subprocess.run(args,
                       input='\n'.join(stdin_lines),
                       stdout=subprocess.PIPE,
                       encoding='utf-8',
                       check=True)
    stdout = p.stdout.removesuffix('\n')
    if not stdout:
        return []
    return stdout.split('\n')


def _get_directory(path, path_parts):
    name, path_parts = path_parts[0], path_parts[1:]
    children = [_get_directory(path, path_parts)] if path_parts else []
    return Directory(path=(path if not path_parts else None),
                     name=name,
                     children=children)


def _group_directories(directories):
    name_directories = {}
    for i in directories:
        name_directories.setdefault(i.name, []).append(i)

    for name, directories in name_directories.items():
        path = next((i.path for i in directories if i.path), None)
        children = list(_group_directories(
            itertools.chain.from_iterable(i.children for i in directories)))
        yield Directory(path=path,
                        name=name,
                        children=children)


def _reduce_directory(directory):
    while not directory.path and len(directory.children) == 1:
        child = directory.children[0]
        directory = child._replace(name=str(Path(directory.name) / child.name))

    return directory._replace(children=[_reduce_directory(child)
                                        for child in directory.children])


def _parse_messages(lines):
    messages = []
    while lines:
        path = lines[0]
        depth = 0
        while path[0] == ' ':
            depth += 1
            path = path[1:]

        status = Status(lines[1])
        if not Path(path).exists():
            status = Status.VIRTUAL

        message = Message(path=path,
                          status=status,
                          subject=lines[2],
                          sender=lines[3],
                          date=lines[4],
                          children=[])
        lines = lines[5:]

        children = messages
        while depth:
            if children:
                children = children[-1].children
            depth -= 1

        children.append(message)

    return messages
