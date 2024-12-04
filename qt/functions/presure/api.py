import requests
from PySide2.QtWidgets import QMessageBox

from libs.presureShare import AC


'''
根据相关参数查询ota升级的版本信息
参数：
deviceId: 设备号

返回：
False: 执行错误
key:版本的id   value:版本号
'''
def selectVersionMap(deviceId: str):
    if deviceId is None or deviceId == '':
        QMessageBox.information(None, "版本获取", "设备号不能为空")
        return False
    body = {
        "deviceId": deviceId
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': AC.token
    }
    response = requests.session().post("http://localhost:8081/device-service/pressure/ota/versions", json=body, headers=headers)
    if response.status_code != 200:
        QMessageBox.about(None, "查询结果", f"查询失败，状态码：{response.status_code}")
        return False
    resJson = response.json()
    if resJson['code'] != 200:
        QMessageBox.about(None, "查询结果", f"查询失败：{resJson['message']}")
        return False
    return {item['id']: item['packageVersion'] for item in resJson['data']}
