from threading import Thread

import requests
from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog

from createTask import Win_create_task
from libs.fileUtil import ui_load
from libs.presureShare import AC, HP


class Win_home(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.ui = ui_load('home.ui')
        self.ui.addOtaTaskBtn.clicked.connect(self.addOtaTask)
        self.ui.refreshOtaTaskBtn.clicked.connect(self.refreshOtaTask)
        self.ui.lastPageBtn.clicked.connect(self.lastPage)
        self.ui.nextPageBtn.clicked.connect(self.nextPage)
        self.ui.exportPressureOtaBtn.clicked.connect(self.exportPressureOta)

        self.setWindowFlags(self.ui.windowFlags() | Qt.FramelessWindowHint | Qt.Popup | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 加载弹窗
        self.createTask = None

        self.refreshTable()

        # 连接到信号槽
        self.request_failed.connect(self.show_request_failed_message)

    def addOtaTask(self):
        self.createTask = Win_create_task(self) if self.createTask is None else self.createTask
        self.createTask.showNewConnect()

    def refreshOtaTask(self):
        self.refreshTable()

    def lastPage(self):
        pageNo = HP.pageNo
        if pageNo <= 1:
            QMessageBox.about(None, "翻页提示", "当前已经是首页")
            return
        HP.pageNo = HP.pageNo - 1
        self.refreshTable()

    def nextPage(self):
        pageNo = HP.pageNo
        if pageNo + 1 >= HP.pageNo:
            QMessageBox.about(None, "翻页提示", "当前已经是最后一页")
            return
        HP.pageNo = HP.pageNo + 1
        self.refreshTable()

    def exportPressureOta(self):
        taskName = self.ui.pressureNameEdit.text()
        if taskName is None or taskName == '':
            QMessageBox.about(None, "参数异常", "缺少必要的压测批次名")
            return
        body = {'name': taskName}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': AC.token
        }
        response = requests.session().post('https://si.kalman-navigation.com/device-service/pressure/ota/export', json=body, headers=headers)
        if response.status_code != 200:
            QMessageBox.about(None, "下载失败", "请求数据源异常")
            return
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "保存文件", "压测结果.xlsx", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'wb') as file:
                file.write(response.content)
            QMessageBox.about(None, "下载成功", f"文件已保存至: {fileName}")
        else:
            QMessageBox.about(None, "下载失败", f"无法下载文件，状态码: {response.status_code}")


    def refreshTable(self):
        def doRefresh():
            pressureName = self.ui.pressureNameEdit.text()
            # 请求数据
            headers = {
                'Content-Type': 'application/json',
                'Authorization': AC.token
            }
            body = {
                "pageNo": HP.pageNo,
                "pageSize": HP.pageSize
            }
            if pressureName is not None and pressureName.strip() != '':
                body["name"] = pressureName
            resJson = requests.session().post("https://si.kalman-navigation.com/device-service/pressure/ota/page", json=body, headers=headers)
            data = resJson.json()
            if resJson.status_code != 200 or data['code'] != 200:
                self.request_failed.emit(f"更新ota压测列表失败,状态码: {data['message']}")
                return
            HP.totalPage = data['total']
            # 清空表格内容
            self.ui.taskTableWidget.clearContents()
            self.ui.taskTableWidget.setRowCount(0)

            if len(data['data']) == 0:
                return
            def setItem(row, col, one):
                if one is None or one == '':
                    return
                oneItem = QTableWidgetItem(str(one))
                oneItem.setFlags(oneItem.flags() & ~Qt.ItemIsEditable)
                self.ui.taskTableWidget.setItem(row, col, oneItem)

            # 刷新表格数据
            for item in data['data']:
                rowPosition = self.ui.taskTableWidget.rowCount()
                self.ui.taskTableWidget.insertRow(rowPosition)
                setItem(rowPosition, 0, item['deviceId'])
                setItem(rowPosition, 1, item['name'])
                setItem(rowPosition, 2, ','.join(f'{one}' for one in item['packageNameList']))
                setItem(rowPosition, 3, item['currentPackageName'])
                setItem(rowPosition, 4, item['taskId'])
                state = item['state']
                if state == 0:
                    state = '等待升级'
                elif state == 1:
                    state = '升级中'
                elif state == 2:
                    state = '暂停执行'
                elif state == 3:
                    state = '升级结束'
                setItem(rowPosition, 5, state)
                setItem(rowPosition, 6, item['startTime'])
                setItem(rowPosition, 7, item['endTime'])

        thread = Thread(target=doRefresh)
        thread.start()

    # 定义一个信号
    request_failed = Signal(str)

    # @Slot(str)
    def show_request_failed_message(self, message):
        QMessageBox.about(None, "请求失败", message)

