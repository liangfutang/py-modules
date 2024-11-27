from threading import Thread

import requests
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout, QMessageBox, QTableWidgetItem

from qt.functions.presure.libs.presureShare import SI
from qt.functions.utils.fileUtil import ui_load


class Win_home(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.ui = ui_load('home.ui')
        self.ui.addOtaTaskBtn.clicked.connect(self.addOtaTask)
        self.ui.refreshOtaTaskBtn.clicked.connect(self.refreshOtaTask)
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
        self.refreshTable()

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

    def refreshOtaTask(self):
        self.refreshTable()

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
        # 提交
        body = {}
        taskName = self.createTaskUi.taskName.text()
        if taskName is not None:
            body["name"] = taskName
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
        body["taskList"] = taskList

        headers = {
            'Content-Type': 'application/json',
            'Authorization': SI.token
        }
        resJson = requests.session().post("https://si.kalman-navigation.com/device-service/pressure/ota/add", json=body, headers=headers)
        if resJson.status_code != 200:
            QMessageBox.about(None, "请求失败", f"创建升级任务失败,状态码: {resJson.status_code}")
            return
        self.refreshTable()
        # 关闭新建任务窗口
        self.alphaWidget.hide()
        self.createTaskUi.hide()

    def refreshTable(self):
        def doRefresh():
            # 请求数据
            headers = {
                'Content-Type': 'application/json',
                'Authorization': SI.token
            }
            body = {}
            resJson = requests.session().post("https://si.kalman-navigation.com/device-service/pressure/ota/page", json=body, headers=headers)
            data = resJson.json()
            if resJson.status_code != 200 or data['code'] != 200:
                QMessageBox.about(None, "请求失败", f"更新ota压测列表失败,状态码: {resJson.status_code}")
                return
            # 清空表格内容
            self.ui.taskTableWidget.clearContents()
            self.ui.taskTableWidget.setRowCount(0)

            if len(data['data']) == 0:
                return
            # 刷新表格数据
            for item in data['data']:
                rowPosition = self.ui.taskTableWidget.rowCount()
                self.ui.taskTableWidget.insertRow(rowPosition)
                self.ui.taskTableWidget.setItem(rowPosition, 0,  QTableWidgetItem(str(item['deviceId'])))
                self.ui.taskTableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(item['name'])))
                self.ui.taskTableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(item['versions'])))
                self.ui.taskTableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(item['currentVersion'])))
                self.ui.taskTableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(item['taskId'])))
                self.ui.taskTableWidget.setItem(rowPosition, 5, QTableWidgetItem(str(item['state'])))
                self.ui.taskTableWidget.setItem(rowPosition, 6, QTableWidgetItem(str(item['startTime'])))
                self.ui.taskTableWidget.setItem(rowPosition, 7, QTableWidgetItem(str(item['endTime'])))

        thread = Thread(target=doRefresh)
        thread.start()
