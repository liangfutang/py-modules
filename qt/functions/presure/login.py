import requests
from PySide2.QtWidgets import QWidget, QMessageBox

from qt.functions.presure.home import Win_home
from qt.functions.presure.libs.presureShare import AC, SI
from qt.functions.utils.fileUtil import ui_load
from qt.functions.utils.paramValid import blank


class Win_Login(QWidget):
    def __init__(self):
        self.ui = ui_load('login.ui')
        self.ui.cencalBtn.clicked.connect(self.cancalHandle)
        self.ui.confirmBtn.clicked.connect(self.confirmHandle)
        self.ui.passwordEdit.returnPressed.connect(self.confirmHandle)

    def cancalHandle(self):
        self.ui.close()

    def confirmHandle(self):
        account = self.ui.accountEdit.text().strip()
        password = self.ui.passwordEdit.text().strip()
        # if blank(account) or blank(password):
        #     QMessageBox.about(None, "登录失败", "账号或密码不能为空")
        #     return
        # resJson = requests.session().post("https://si.kalman-navigation.com/auth-service/auth/loginWithoutCaptcha",
        #                                   json={"name": account, "password": password}).json()
        # if resJson["code"] != 200 or blank(resJson["data"]["accessToken"]):
        #     QMessageBox.about(None, "登录失败", "账号或密码错误")
        #     return
        # # 登录成功
        # # 保存token
        # AC.token = resJson["data"]["accessToken"]
        # 跳转
        SI.mainWin = Win_home()
        SI.mainWin.ui.show()
        # 影藏当前登录页面
        # self.ui.edit_password.setText('')
        self.ui.hide()