from threading import Thread

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QCheckBox

from api import VersionSelect, ConfirmNewTask
from libs.fileUtil import ui_load


class Win_create_task:
    def __init__(self, win_home):
        super().__init__()
        self.win_home = win_home
        parent_ui = win_home.ui
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
        # 设置单元格事件
        self.createTaskUi.newConnectForm.itemChanged.connect(self.cell_event)
        # 异步处理获取版本信息链接到信号槽
        self.versionSelect = VersionSelect()
        self.versionSelect.versionSignal.connect(self.operate_version)
        self.confirmNewTask = ConfirmNewTask()
        self.confirmNewTask.confirmSignal.connect(win_home.refreshTable)
        # 隐藏弹窗
        self.alphaWidget.hide()
        self.createTaskUi.hide()

    def cell_event(self, item):
        if item is None or item.column() != 0:
            return
        thread = Thread(target=self.versionSelect.selectVersionMap, args=(item,))
        thread.start()

    def operate_version(self, item, versionIdMap):
        if not versionIdMap:
            return
        container_widget = QWidget()
        layout = QVBoxLayout(container_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        for (id, version) in versionIdMap.items():
            checkbox = QCheckBox(version)
            checkbox.setProperty("versionId", id)
            layout.addWidget(checkbox)
        self.createTaskUi.newConnectForm.setCellWidget(item.row(), item.column() + 1, container_widget)
        self.createTaskUi.newConnectForm.resizeRowsToContents()

    def cancalNewConnect(self):
        self.createTaskUi.newConnectForm.setRowCount(0)
        self.createTaskUi.taskName.setText('')
        self.alphaWidget.hide()
        self.createTaskUi.hide()

    def showNewConnect(self):
        self.alphaWidget.show()
        self.createTaskUi.show()
    def confirmNewConnect(self):
        # 提交
        thread = Thread(target=self.confirmNewTask.confirm, args=(self.createTaskUi,))
        thread.start()
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
