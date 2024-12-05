import requests
from PySide2.QtCore import Signal, QObject
from PySide2.QtWidgets import QMessageBox, QTableWidgetItem, QWidget, QCheckBox

from libs.presureShare import AC

'''
根据相关参数查询ota升级的版本信息
'''
class VersionSelect(QObject):
    versionSingle = Signal(QTableWidgetItem, dict)

    def selectVersionMap(self, item):
        deviceId = item.text()
        if deviceId is None or deviceId.strip() == '':
            QMessageBox.information(None, "版本获取", "设备号不能为空")
            return
        body = {
            "deviceId": deviceId.strip()
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': AC.token
        }
        try:
            response = requests.session().post("https://si.kalman-navigation.com/device-service/pressure/ota/versions", json=body, headers=headers)
            if response.status_code != 200:
                QMessageBox.about(None, "查询结果", f"查询失败，状态码：{response.status_code}")
                return
            resJson = response.json()
            if resJson['code'] != 200:
                QMessageBox.about(None, "查询结果", f"查询失败：{resJson['message']}")
                return
            self.versionSingle.emit(item, {item['id']: item['packageVersion'] for item in resJson['data']})
        except Exception as e:
            QMessageBox.critical(None, "查询结果", f"发生异常：{str(e)}")

'''
提交新升级任务
'''
class ConfirmNewTask(QObject):
    confirmSingle = Signal()
    def confirm(self, ui):
        taskName = ui.taskName.text()
        if taskName is None or taskName.strip() == '':
            QMessageBox.about(None, "创建失败", "升级批次名不能为空")
            return
        body = {"name": taskName.strip()}
        taskList = []
        for row in range(ui.newConnectForm.rowCount()):
            one = {}
            # 设备号
            deviceId = ui.newConnectForm.item(row, 0).text()
            if deviceId is None or deviceId.strip() == '':
                QMessageBox.about(None, "创建失败", "设备号不能为空")
                return
            one['deviceId'] = deviceId.strip()
            # 升级版本
            versionsWidget = ui.newConnectForm.cellWidget(row, 1)
            otaVersionIdList = []
            if versionsWidget:
                layout = versionsWidget.layout()
                for index in range(layout.count()):
                    widget = layout.itemAt(index).widget()
                    if isinstance(widget, QCheckBox) and widget.isChecked():
                        otaVersionIdList.append(widget.property("versionId"))

            if not otaVersionIdList:
                QMessageBox.about(None, "创建失败", "设备升级版本不能为空")
                return
            one['otaVersionIdList'] = otaVersionIdList
            # 开始时间
            startTime = ui.newConnectForm.item(row, 2)
            if startTime is not None:
                one['startTime'] = startTime.text()
            # 结束时间
            endTime = ui.newConnectForm.item(row, 3)
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
        resJson = requests.session().post("https://si.kalman-navigation.com/device-service/pressure/ota/add", json=body,
                                          headers=headers)
        if resJson.status_code != 200:
            QMessageBox.about(None, "请求失败", f"创建升级任务失败,状态码: {resJson.status_code}")
            return
        self.confirmSingle.emit()
