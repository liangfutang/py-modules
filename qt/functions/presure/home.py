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


        self.login = ui_load('login.ui')
        self.login.setGeometry((self.ui.width()-self.login.width())/2, (self.ui.height()-self.login.height())/2, self.login.width(), self.login.height())
        self.login.setParent(self.ui)
        loginUiName = self.login.objectName()
        self.login.setStyleSheet('#' + loginUiName + '{background-color:red;}')

    # def resizeEvent(self, event):
    #     self.alphaWidget.resize(self.size())
    #     super(Win_home, self).resizeEvent(event)