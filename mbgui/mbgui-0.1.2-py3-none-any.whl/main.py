from pathlib import Path
import sys

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtUiTools
import PySide6.QtWidgets

from mbgui import mblaze
from mbgui.executor import Executor


icons_path = Path(__file__).parent / 'icons'
main_ui_path = Path(__file__).parent / 'main.ui'


def main():

    def on_directories_changed(current, previous):
        item = directories.model.itemFromIndex(current)
        directory = item.data() if item else None
        messages.set_directory(directory)

    def on_messages_changed(current, pevious):
        item = messages.model.itemFromIndex(current)
        path = item.data() if item else None
        message.set_path(path)

    def on_messages_double_clicked(index):
        item = messages.model.itemFromIndex(index)
        path = item.data() if item else None
        if path:
            print(path)

    app = PySide6.QtWidgets.QApplication(sys.argv)

    executor = Executor()
    icons = {i.stem: PySide6.QtGui.QIcon(str(i))
             for i in icons_path.glob('*.png')}

    directories = Directories(executor, icons, sys.argv[1:])
    messages = Messages(executor, icons)
    message = Message(executor)

    loader = PySide6.QtUiTools.QUiLoader()
    window = loader.load(main_ui_path)

    font = PySide6.QtGui.QFontDatabase.systemFont(
        PySide6.QtGui.QFontDatabase.FixedFont)
    window.message.setFont(font)

    window.vsplitter.setStretchFactor(0, 1)
    window.vsplitter.setStretchFactor(1, 2)

    window.directories.setModel(directories.model)
    model = window.directories.selectionModel()
    model.currentChanged.connect(on_directories_changed)

    header = window.directories.header()
    header.setSectionResizeMode(0, PySide6.QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(1, PySide6.QtWidgets.QHeaderView.Interactive)
    header.setSectionResizeMode(2, PySide6.QtWidgets.QHeaderView.Interactive)

    window.messages.setModel(messages.model)
    model = window.messages.selectionModel()
    model.currentChanged.connect(on_messages_changed)
    window.messages.doubleClicked.connect(on_messages_double_clicked)

    header = window.messages.header()
    header.setSectionResizeMode(0, PySide6.QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(1, PySide6.QtWidgets.QHeaderView.Interactive)
    header.setSectionResizeMode(2, PySide6.QtWidgets.QHeaderView.Interactive)

    message.change.connect(window.message.setText)

    window.show()

    sys.exit(app.exec())


class Directories:

    def __init__(self, executor, icons, paths):
        self._executor = executor
        self._icons = icons
        self._model = PySide6.QtGui.QStandardItemModel()
        self._model.setHorizontalHeaderLabels(['Directory', 'Unseed', 'Total'])
        self._get_directories(paths)

    @property
    def model(self) -> PySide6.QtCore.QAbstractItemModel:
        return self._model

    def _get_directories(self, paths):

        def on_done(directories):
            for directory in directories:
                self._model.appendRow(create_row(directory))

        def create_row(directory):
            icon = self._icons['inbox-16' if directory.path
                               else 'folder-16']

            items = [PySide6.QtGui.QStandardItem(icon, directory.name),
                     PySide6.QtGui.QStandardItem(''),
                     PySide6.QtGui.QStandardItem('')]

            for item in items:
                item.setData(directory.path)

            if directory.path:
                self._get_directory_unseen(items[1], directory.path)
                self._get_directory_total(items[2], directory.path)

            for child in directory.children:
                items[0].appendRow(create_row(child))

            return items

        self._executor.call_worker(mblaze.get_directories, paths,
                                   done_cb=on_done)

    def _get_directory_unseen(self, item, path):

        def on_done(count):
            item.setText(str(count))

        self._executor.call_worker(mblaze.get_directory_unseen, path,
                                   done_cb=on_done)

    def _get_directory_total(self, item, path):

        def on_done(count):
            item.setText(str(count))

        self._executor.call_worker(mblaze.get_directory_total, path,
                                   done_cb=on_done)


class Messages:

    def __init__(self, executor: Executor, icons):
        self._executor = executor
        self._icons = icons
        self._model = PySide6.QtGui.QStandardItemModel()
        self._model.setHorizontalHeaderLabels(['Subject', 'Sender', 'Date'])
        self._directory = None

    @property
    def model(self) -> PySide6.QtCore.QAbstractItemModel:
        return self._model

    def set_directory(self, directory: str):
        if self._directory == directory:
            return

        self._directory = directory
        self._model.setRowCount(0)

        if directory:
            self._get_messages(directory)

    def _get_messages(self, directory):

        def on_done(messages):
            if self._directory != directory:
                return

            for message in messages:
                self._model.appendRow(create_row(message))

        def create_row(message):
            icon = _status_icon(message.status)
            icon = self._icons[f'{icon}-16'] if icon else None

            items = [PySide6.QtGui.QStandardItem(icon, message.subject),
                     PySide6.QtGui.QStandardItem(message.sender),
                     PySide6.QtGui.QStandardItem(message.date)]

            for item in items:
                item.setData(message.path)

            for child in message.children:
                items[0].appendRow(create_row(child))

            return items

        self._executor.call_worker(mblaze.get_messages, directory,
                                   done_cb=on_done)

    def _on_messages(self, directory, messages):
        if directory != self._selected_directory:
            return


class Message(PySide6.QtCore.QObject):

    change = PySide6.QtCore.Signal(str)

    def __init__(self, executor):
        super().__init__()
        self._executor = executor
        self._path = None

    def set_path(self, path):
        if self._path == path:
            return

        self._path = path
        self.change.emit('')

        if path:
            self._get_message(path)

    def _get_message(self, path):

        def on_done(text):
            if self._path != path:
                return

            self.change.emit(text)

        self._executor.call_worker(mblaze.get_message, path,
                                   done_cb=on_done)


def _status_icon(status):
    if status == mblaze.Status.SEEN:
        return 'file'

    if status == mblaze.Status.FLAGGED:
        return 'flag'

    if status == mblaze.Status.UNSEEN:
        return 'mail'

    if status == mblaze.Status.TRASHED:
        return 'trash'

    if status == mblaze.Status.VIRTUAL:
        return 'eye-off'

    raise ValueError('unsupported status')


if __name__ == '__main__':
    main()
