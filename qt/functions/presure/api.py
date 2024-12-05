import requests
from PySide2.QtCore import Signal, QObject
from PySide2.QtWidgets import QMessageBox, QTableWidgetItem

from libs.presureShare import AC

'''
根据相关参数查询ota升级的版本信息
'''
class VersionSelect(QObject):
    versionSingle = Signal(QTableWidgetItem, dict)

    def selectVersionMap(self, item):
        deviceId = item.text()
        if deviceId is None or deviceId == '':
            QMessageBox.information(None, "版本获取", "设备号不能为空")
            return
        body = {
            "deviceId": deviceId
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': AC.token
        }
        try:
            response = requests.session().post("http://localhost:8081/device-service/pressure/ota/versions", json=body, headers=headers)
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
