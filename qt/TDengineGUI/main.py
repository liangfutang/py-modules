# -*- coding: utf-8 -*-
import sys

from PySide2 import QtCore
from PySide2.QtCore import QRect, QMetaObject, QCoreApplication, QPropertyAnimation, QEasingCurve, QPointF, QPoint, \
    QSize
from PySide2.QtGui import Qt, QMouseEvent, QCursor, QPixmap
from PySide2.QtWidgets import QWidget, QTabWidget, QHBoxLayout, QListWidget, QVBoxLayout, QLabel, QPushButton, \
    QSpacerItem, QSizePolicy, QMenuBar, QStatusBar, QApplication, QMainWindow, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"#data_show {\n"
            "	border: 1px solid #868686;\n"
            "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#data_show{\n"
            "  border-size: 1px\n"
            "}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        # self.tabWidget.setGeometry(QRect(180, 73, 486, 271))
        self.stableTab = QWidget()
        self.stableTab.setObjectName(u"stableTab")
        self.horizontalLayout_4 = QHBoxLayout(self.stableTab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stableListShow = QListWidget(self.stableTab)
        self.stableListShow.setObjectName(u"stableListShow")

        self.horizontalLayout_3.addWidget(self.stableListShow)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.stableTab)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.stableTab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.stableTab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.data_show = QWidget(self.stableTab)
        self.data_show.setObjectName(u"data_show")
        self.verticalLayout_3 = QVBoxLayout(self.data_show)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.noDataLabel = QLabel(self.data_show)
        self.noDataLabel.setObjectName(u"noDataLabel")

        self.verticalLayout_3.addWidget(self.noDataLabel)

        self.verticalLayout.addWidget(self.data_show)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.stableTab, "")
        self.tableTab = QWidget()
        self.tableTab.setObjectName(u"tableTab")
        self.horizontalLayout_5 = QHBoxLayout(self.tableTab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_3 = QPushButton(self.tableTab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.tabWidget.addTab(self.tableTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u8303\u56f4", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009\u6761\u4ef6", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u6570\u636e", None))
        self.noDataLabel.setText(QCoreApplication.translate("MainWindow", u"\u6682\u65e0\u6570\u636e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stableTab), QCoreApplication.translate("MainWindow", u"\u8d85\u7ea7\u8868", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tableTab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

class DrawerWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(DrawerWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('DrawerWidget{background:white;}')
        self.setObjectName(u"side")

        # self.sideBar = QWidget(self.centralwidget)
        # self.sideBar.setObjectName(u"sideBar")
        # self.sideBar.setGeometry(QRect(10, 70, 141, 271))
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.sideNewConnectBtn = QPushButton(self)
        self.sideNewConnectBtn.setObjectName(u"sideNewConnectBtn")
        self.sideNewConnectBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sideNewConnectBtn.setStyleSheet(u"#sideNewConnectBtn {\n"
                                             "	background-color: #ecf5ff; /* \u6d45\u84dd\u8272\u80cc\u666f */\n"
                                             "    border: 0.5px solid #007bff;\n"
                                             "    color: #409eff; /* \u6587\u5b57\u989c\u8272\u4e3a\u6df1\u84dd\u8272 */\n"
                                             "    padding: 10px 20px; /* \u5185\u8fb9\u8ddd */\n"
                                             "    text-align: center;\n"
                                             "    font-size: 13px; /* \u5b57\u4f53\u5927\u5c0f */\n"
                                             "    border-radius: 5px; /* \u5706\u89d2 */\n"
                                             "}\n"
                                             "\n"
                                             "#sideNewConnectBtn:hover {\n"
                                             "	background-color: #409eff;\n"
                                             "	color:#fff;\n"
                                             "}")

        self.verticalLayout_2.addWidget(self.sideNewConnectBtn)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None))
        self.sideNewConnectBtn.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u8fde\u63a5", None))

        self.sideNewConnectBtn.clicked.connect(self.handleNewConnection)
        # self.newConnectCloseLab

    def handleNewConnection(self):
        self.newConnection = NewConnection(self.parent().parent())
        self.newConnection.setWidget(NewConnectionWidget(self.newConnection))
        self.newConnection.show()


class CDrawer(QWidget):

    def __init__(self, *args, stretch=1 / 3, direction=0, widget=None, **kwargs):
        super(CDrawer, self).__init__(*args, **kwargs)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.Popup | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 进入动画
        self.animIn = QPropertyAnimation(
            self, duration=500, easingCurve=QEasingCurve.OutCubic)
        self.animIn.setPropertyName(b'pos')
        # 离开动画
        self.animOut = QPropertyAnimation(
            self, duration=500, finished=self.onAnimOutEnd,
            easingCurve=QEasingCurve.OutCubic)
        self.animOut.setPropertyName(b'pos')
        self.animOut.setDuration(500)
        self.stretch = max(0.1, min(stretch, 0.9))  # 占比
        # 半透明背景
        self.alphaWidget = QWidget(
            self, objectName='CDrawer_alphaWidget',
            styleSheet='#CDrawer_alphaWidget{background:rgba(55,55,55,100);}')
        self.alphaWidget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setWidget(widget)  # 子控件

    def resizeEvent(self, event):
        self.alphaWidget.resize(self.size())
        super(CDrawer, self).resizeEvent(event)

    def mousePressEvent(self, event):
        pos = event.pos()
        if pos.x() >= 0 and pos.y() >= 0 and self.childAt(pos) == None and self.widget:
            if not self.widget.geometry().contains(pos):
                self.animationOut()
                return
        super(CDrawer, self).mousePressEvent(event)

    def show(self):
        super(CDrawer, self).show()
        parent = self.parent().window() if self.parent() else self.window()
        if not parent or not self.widget:
            return
        # 设置Drawer大小和主窗口一致
        self.setGeometry(parent.geometry())
        geometry = self.geometry()
        self.animationIn(geometry)

    def animationIn(self, geometry):
        """进入动画
        :param geometry:
        """
        # 左侧抽屉
        self.widget.setGeometry(
            0, 0, int(geometry.width() * self.stretch), geometry.height())
        self.widget.hide()
        self.animIn.setStartValue(QPoint(-self.widget.width(), 0))
        self.animIn.setEndValue(QPoint(0, 0))
        self.animIn.start()
        self.widget.show()

    def animationOut(self):
        """离开动画
        """
        self.animIn.stop()  # 停止进入动画
        geometry = self.widget.geometry()
        # 左侧抽屉
        self.animOut.setStartValue(geometry.topLeft())
        self.animOut.setEndValue(QPoint(-self.widget.width(), 0))
        self.animOut.start()

    def onAnimOutEnd(self):
        """离开动画结束
        """
        # 模拟点击外侧关闭
        QApplication.sendEvent(self, QMouseEvent(
            QMouseEvent.MouseButtonPress, QPointF(-1, -1), Qt.LeftButton, Qt.NoButton, Qt.NoModifier))

    def setWidget(self, widget):
        """设置子控件
        :param widget:
        """
        self.widget = widget
        if widget:
            widget.setParent(self)
            self.animIn.setTargetObject(widget)
            self.animOut.setTargetObject(widget)


class NewConnectionWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(NewConnectionWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('NewConnectionWidget{background:white;}')
        self.setObjectName(u"side")

        # self.widget = QWidget(self.centralwidget)
        # self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.newConnectCloseLab = QLabel(self)
        self.newConnectCloseLab.setObjectName(u"newConnectCloseLab")
        self.newConnectCloseLab.setMinimumSize(QSize(30, 30))
        self.newConnectCloseLab.setMaximumSize(QSize(30, 30))
        self.newConnectCloseLab.setCursor(QCursor(Qt.PointingHandCursor))
        self.newConnectCloseLab.setStyleSheet(u"#newConnectCloseLab {\n"
                                              "	color: rgb(85, 170, 255);\n"
                                              "}")
        self.newConnectCloseLab.setPixmap(QPixmap(u"./images/close_win.png"))
        self.newConnectCloseLab.setScaledContents(True)
        self.newConnectCloseLab.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.newConnectCloseLab)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.newConnNameEdit = QLineEdit(self)
        self.newConnNameEdit.setObjectName(u"newConnNameEdit")

        self.horizontalLayout_6.addWidget(self.newConnNameEdit)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 6)
        self.horizontalLayout_6.setStretch(3, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_6 = QLabel(self)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.newConnHostEdit = QLineEdit(self)
        self.newConnHostEdit.setObjectName(u"newConnHostEdit")

        self.horizontalLayout_7.addWidget(self.newConnHostEdit)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 6)
        self.horizontalLayout_7.setStretch(3, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.label_7 = QLabel(self)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.newConnPortEdit = QLineEdit(self)
        self.newConnPortEdit.setObjectName(u"newConnPortEdit")

        self.horizontalLayout_8.addWidget(self.newConnPortEdit)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 6)
        self.horizontalLayout_8.setStretch(3, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.label_8 = QLabel(self)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.newConnUserEdit = QLineEdit(self)
        self.newConnUserEdit.setObjectName(u"newConnUserEdit")

        self.horizontalLayout_9.addWidget(self.newConnUserEdit)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 6)
        self.horizontalLayout_9.setStretch(3, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.label_9 = QLabel(self)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.newPassNameEdit = QLineEdit(self)
        self.newPassNameEdit.setObjectName(u"newPassNameEdit")

        self.horizontalLayout_10.addWidget(self.newPassNameEdit)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 6)
        self.horizontalLayout_10.setStretch(3, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.cancalBtn = QPushButton(self)
        self.cancalBtn.setObjectName(u"cancalBtn")
        self.cancalBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.cancalBtn)

        self.confirmBtn = QPushButton(self)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirmBtn.setStyleSheet(u"#confirmBtn {\n"
                                      "	background-color: rgb(64, 158, 255);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}")

        self.horizontalLayout_11.addWidget(self.confirmBtn)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        # retranslateUi
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u8fde\u63a5", None))
        self.newConnectCloseLab.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.cancalBtn.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.confirmBtn.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))

        self.cancalBtn.clicked.connect(self.cancalNewConnect)
        self.newConnectCloseLab.mouseReleaseEvent = self.on_click_close_new_conn

    def cancalNewConnect(self):
        self.parent().alphaWidget.close()
        self.close()

    def on_click_close_new_conn(self, event):
        # 检查是否是左键释放
        if event.button() == QtCore.Qt.LeftButton:
            # 关闭窗口
            self.cancalNewConnect()

class NewConnection(QWidget):

    LEFT, TOP, RIGHT, BOTTOM = range(4)

    def __init__(self, *args, widget=None, **kwargs):
        super(NewConnection, self).__init__(*args, **kwargs)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.Popup | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 半透明背景
        self.alphaWidget = QWidget(
            self, objectName='CDrawer_alphaWidget',
            styleSheet='#CDrawer_alphaWidget{background:rgba(55,55,55,100);}')
        self.alphaWidget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setWidget(widget)  # 子控件


    def resizeEvent(self, event):
        self.alphaWidget.resize(self.size())
        super(NewConnection, self).resizeEvent(event)

    def mousePressEvent(self, event):
        pos = event.pos()
        if pos.x() >= 0 and pos.y() >= 0 and self.childAt(pos) == None and self.widget:
            if not self.widget.geometry().contains(pos):
                self.close()
                return
        super(NewConnection, self).mousePressEvent(event)

    def show(self):
        super(NewConnection, self).show()
        parent = self.parent().window() if self.parent() else self.window()
        if not parent or not self.widget:
            return
        # 设置Drawer大小和主窗口一致
        self.setGeometry(parent.geometry())
        geometry = self.geometry()
        self.widget.setGeometry(
            (geometry.width()-400)/2, (geometry.height()-400)/2, 400, 400)
        self.widget.hide()
        self.widget.show()

    def setWidget(self, widget):
        """设置子控件
        :param widget:
        """
        self.widget = widget
        if widget:
            widget.setParent(self)

    def setEasingCurve(self, easingCurve):
        """设置动画曲线
        :param easingCurve:
        """
        self.animIn.setEasingCurve(easingCurve)

    def getStretch(self):
        """获取占比
        """
        return self.stretch

    def setStretch(self, stretch):
        """设置占比
        :param stretch:
        """
        self.stretch = max(0.1, min(stretch, 0.9))

    def getDirection(self):
        """获取方向
        """
        return self.direction

    def setDirection(self, direction):
        """设置方向
        :param direction:
        """
        direction = int(direction)
        if direction < 0 or direction > 3:
            direction = self.LEFT
        self.direction = direction

class Window():
    def __init__(self, *args, **kwargs):
        self.w = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.w)
        self.ui.pushButton.clicked.connect(self.doOpenLeft)
        self.ui.pushButton_2.clicked.connect(self.doOpenLeft1)
    def doOpenLeft(self):
        if not hasattr(self, 'leftDrawer'):
            self.leftDrawer = CDrawer(self.w)
            self.leftDrawer.setWidget(DrawerWidget(self.leftDrawer))
        self.leftDrawer.show()

    def doOpenLeft1(self):
        if not hasattr(self, 'newConnection'):
            self.newConnection = NewConnection(self.w)
            self.newConnection.setWidget(NewConnectionWidget(self.newConnection))
        self.newConnection.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.w.show()
    sys.exit(app.exec_())
