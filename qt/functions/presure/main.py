from PySide2.QtWidgets import QApplication

from qt.functions.presure.libs.presureShare import SI
from qt.functions.presure.login import Win_Login

app = QApplication([])
SI.loginWin = Win_Login()
SI.loginWin.ui.show()
app.exec_()
