# 登录进行学生管理

from PySide2.QtWidgets import QApplication, QMessageBox

from qt. functions.utils.fileUtil import ui_load
from qt.functions.hydm.libs.hydmShare import SI
import requests


class Win_Login:
    def __init__(self):
        self.ui = ui_load('login.ui')
        # 点击登录按钮和密码框回车的时候提交登录
        self.ui.btn_login.clicked.connect(self.onSignIn)
        self.ui.edit_password.returnPressed.connect(self.onSignIn)

    def onSignIn(self):
        username = self.ui.edit_username.text().strip()
        password = self.ui.edit_password.text().strip()
        print(username, password)
        if username is None or username == '' or password is None or password == '':
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("提示")  # 显式设置标题
            msg_box.setText("用户名或密码不能为空")  # 显式设置内容
            msg_box.exec_()
            return
        # 提交登录请求
        resJson = requests.session().post("http://localhost:8000/hydm/login", json={"username": username, "password": password}).json()
        if resJson['code'] != '0':
            QMessageBox.about(None, "登录结果", "登录失败：" + resJson['message'])
            return
        SI.mainWin = Win_main()
        SI.mainWin.ui.show()

        self.ui.edit_password.setText('')
        self.ui.hide()
class Win_main:
    def __init__(self):
        self.ui = ui_load('main.ui')
        self.ui.actionExit.triggered.connect(self.onSignOut)

    def onSignOut(self):
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()


app = QApplication([])
SI.loginWin = Win_Login()
SI.loginWin.ui.show()
app.exec_()
