from PySide2.QtWidgets import QMainWindow

from qt.functions.utils.fileUtil import ui_load


class Win_home(QMainWindow):
    def __init__(self):
        self.ui = ui_load('home.ui')