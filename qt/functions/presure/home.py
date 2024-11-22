from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QWidget

from qt.functions.utils.fileUtil import ui_load


class Win_home(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.ui = ui_load('home.ui')

        self.setWindowFlags(self.ui.windowFlags() | Qt.FramelessWindowHint | Qt.Popup | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 半透明背景
        self.alphaWidget = QWidget(
            self.ui, objectName='aaa',
            styleSheet='#aaa{background:rgba(55,55,55,100);}')
        self.alphaWidget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.alphaWidget.resize(self.ui.size())  # 设置 alphaWidget 的大小
        # 主界面上弹窗显示
        self.createTaskUi = ui_load('createTask.ui')
        self.createTaskUi.setGeometry((self.ui.width()-self.createTaskUi.width())/2, (self.ui.height()-self.createTaskUi.height())/2, self.createTaskUi.width(), self.createTaskUi.height())
        self.createTaskUi.setParent(self.ui)
