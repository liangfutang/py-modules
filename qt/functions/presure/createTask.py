import requests
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QMessageBox, QHBoxLayout, QPushButton

from libs.fileUtil import ui_load
from libs.presureShare import AC


class Win_create_task:
    def __init__(self, parent_ui):
        super().__init__()  # 调用父类的构造函数
        # 半透明背景
        self.alphaWidget = QWidget(
            parent_ui, objectName='aaa',
            styleSheet='#aaa{background:rgba(55,55,55,100);}')
        self.alphaWidget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.alphaWidget.resize(parent_ui.size())  # 设置 alphaWidget 的大小
        # 主界面上弹窗显示
        self.createTaskUi = ui_load('createTask.ui')
        self.createTaskUi.setGeometry((parent_ui.width()-self.createTaskUi.width())/2, (parent_ui.height()-self.createTaskUi.height())/2, self.createTaskUi.width(), self.createTaskUi.height())
        self.createTaskUi.setParent(parent_ui)
        self.createTaskUi.cancalNewConnectBtn.clicked.connect(self.cancalNewConnect)
        self.createTaskUi.confirmNewConnectBtn.clicked.connect(self.confirmNewConnect)
        self.createTaskUi.addOneDeviceBtn.clicked.connect(self.addOneDevice)
        # 隐藏弹窗
        self.alphaWidget.hide()
        self.createTaskUi.hide()

    def cancalNewConnect(self):
        self.createTaskUi.newConnectForm.setRowCount(0)
        self.alphaWidget.hide()
        self.createTaskUi.hide()

    def showNewConnect(self):
        self.alphaWidget.show()
        self.createTaskUi.show()
    def confirmNewConnect(self):
        # 提交
        taskName = self.createTaskUi.taskName.text()
        if taskName is None or taskName.strip() == '':
            QMessageBox.about(None, "创建失败", "升级批次名不能为空")
            return
        body = {"name": taskName.strip()}
        taskList = []
        for row in range(self.createTaskUi.newConnectForm.rowCount()):
            one = {}
            # 设备号
            deviceId = self.createTaskUi.newConnectForm.item(row, 0).text()
            if deviceId is None or deviceId == '':
                QMessageBox.about(None, "创建失败", "设备号不能为空")
                return
            one['deviceId'] = deviceId
            # 升级版本
            versions = self.createTaskUi.newConnectForm.item(row, 1).text()
            if versions is None or versions == '':
                QMessageBox.about(None, "创建失败", "设备升级版本不能为空")
                return
            one['otaVersionIdList'] = versions.split(',')
            # 开始时间
            startTime = self.createTaskUi.newConnectForm.item(row, 2)
            if startTime is not None:
                one['startTime'] = startTime.text()
            # 结束时间
            endTime = self.createTaskUi.newConnectForm.item(row, 3)
            if endTime is not None:
                one['endTime'] = endTime.text()

            taskList.append(one)
        if not taskList:
            QMessageBox.about(None, "创建失败", "至少要有一个升级设备详情")
            return
        body["taskList"] = taskList

        headers = {
            'Content-Type': 'application/json',
            'Authorization': AC.token
        }
        resJson = requests.session().post("https://si.kalman-navigation.com/device-service/pressure/ota/add", json=body, headers=headers)
        if resJson.status_code != 200:
            QMessageBox.about(None, "请求失败", f"创建升级任务失败,状态码: {resJson.status_code}")
            return
        super().refreshTable()
        # 关闭新建任务窗口
        self.alphaWidget.hide()
        self.createTaskUi.hide()

    def addOneDevice(self):
        rowPosition = self.createTaskUi.newConnectForm.rowCount()
        self.createTaskUi.newConnectForm.insertRow(rowPosition)
        # 创建按钮
        addDevice = QPushButton("+")
        addDevice.setFixedHeight(20)
        addDevice.clicked.connect(self.addOneDevice)
        plusDevice = QPushButton("-")
        plusDevice.setFixedHeight(20)
        plusDevice.clicked.connect(lambda r=rowPosition, row=rowPosition: self.plusSelfDevice(r))
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
                    plusBtn.clicked.connect(lambda rc=r, row=r: self.plusSelfDevice(rc))
