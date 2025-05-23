from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit

def handleCacle():
    print("点击统计")

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('统计', window)
button.move(380, 80)
button.clicked.connect(handleCacle)

window.show()

app.exec_()