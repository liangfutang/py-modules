from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout

from qt.functions.utils.fileUtil import ui_load


class Win_home(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.ui = ui_load('home.ui')
        self.ui.addOtaTaskBtn.clicked.connect(self.addOtaTask)
        # 加载列表

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
        self.createTaskUi.cancalNewConnectBtn.clicked.connect(self.cancalNewConnect)
        self.createTaskUi.confirmNewConnectBtn.clicked.connect(self.confirmNewConnect)
        self.createTaskUi.addOneDeviceBtn.clicked.connect(self.addOneDevice)

        # 隐藏弹窗
        self.alphaWidget.hide()
        self.createTaskUi.hide()

    def addOtaTask(self):
        self.alphaWidget.show()
        self.createTaskUi.show()

        # rowPosition = self.ui.taskTableWidget.rowCount()
        # self.ui.taskTableWidget.insertRow(rowPosition)
        # self.ui.taskTableWidget.setItem(rowPosition, 0, QTableWidgetItem('E10050123B00602'))
        # self.ui.taskTableWidget.setItem(rowPosition, 1, QTableWidgetItem('E10050123B00602'))
        # self.ui.taskTableWidget.setItem(rowPosition, 2, QTableWidgetItem('task_1'))
        # self.ui.taskTableWidget.setItem(rowPosition, 3, QTableWidgetItem('1.0,2.0,3.0'))
        # self.ui.taskTableWidget.setItem(rowPosition, 4, QTableWidgetItem('2.0'))
        #
        # for row in range(self.ui.taskTableWidget.rowCount()):
        #     item = self.ui.taskTableWidget.item(row, 4)
        #     if item:
        #         # 移除 Qt.ItemIsEditable 标志
        #         item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def addOneDevice(self):
        rowPosition = self.createTaskUi.newConnectForm.rowCount()
        self.createTaskUi.newConnectForm.insertRow(rowPosition)
        # 创建按钮
        addDevice = QPushButton("+")
        addDevice.clicked.connect(self.addOneDevice)
        plusDevice = QPushButton("-")
        plusDevice.clicked.connect(lambda r=rowPosition: self.plusSelfDevice(r))
        hlayout = QHBoxLayout()
        hlayout.addWidget(addDevice)
        hlayout.addWidget(plusDevice)
        button_widget = QWidget()
        button_widget.setLayout(hlayout)
        self.createTaskUi.newConnectForm.setCellWidget(rowPosition, self.createTaskUi.newConnectForm.columnCount() - 1, button_widget)

    def plusSelfDevice(self, row):
        self.createTaskUi.newConnectForm.removeRow(row)
        for r in range(self.createTaskUi.newConnectForm.rowCount()):
            container = self.createTaskUi.newConnectForm.cellWidget(r, self.createTaskUi.newConnectForm.columnCount() - 1)
            if container:
                layout = container.layout()
                plusBtn = layout.itemAt(1).widget()
                if plusBtn:
                    plusBtn.clicked.disconnect()
                    plusBtn.clicked.connect(lambda rc=r: self.plusSelfDevice(rc))

    def cancalNewConnect(self):
        self.alphaWidget.hide()
        self.createTaskUi.hide()

    def confirmNewConnect(self):
        body = []
        # 提交
        taskName = self.createTaskUi.taskName.text()
        for row in range(self.createTaskUi.newConnectForm.rowCount()):
            one = {"name": taskName}
            # 设备号
            deviceId = self.createTaskUi.newConnectForm.item(row, 0).text()
            one['deviceId'] = deviceId
            # 升级版本
            versions = self.createTaskUi.newConnectForm.item(row, 1).text()
            if len(versions) > 0:
                one['otaVersionIdList'] = versions.split(',')
            # 开始时间
            startTime = self.createTaskUi.newConnectForm.item(row, 2).text()
            one['startTime'] = startTime
            # 结束时间
            endTime = self.createTaskUi.newConnectForm.item(row, 3).text()
            one['endTime'] = endTime

            body.append(one)

        # 关闭新建任务窗口
        self.alphaWidget.hide()
        self.createTaskUi.hide()
