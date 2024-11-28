from PySide2.QtWidgets import QApplication

from libs.presureShare import SI
from login import Win_Login

app = QApplication([])
SI.loginWin = Win_Login()
SI.loginWin.ui.show()
app.exec_()
