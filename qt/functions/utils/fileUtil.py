from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys, os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def ui_load(relative_path):
    ui_file_path = resource_path(relative_path)
    ui_file = QFile(ui_file_path)
    ui_file.open(QFile.ReadOnly)
    ui = QUiLoader().load(ui_file)
    ui_file.close()
    return ui
