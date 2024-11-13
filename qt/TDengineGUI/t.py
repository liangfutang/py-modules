import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide2.QtCore import QPropertyAnimation, QEasingCurve, QRect, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 加载 UI 文件
        loader = QUiLoader()
        self.ui = loader.load("./ui/t1.ui")

        # 设置主窗口
        self.setCentralWidget(self.ui)

        # 获取侧边栏和按钮
        self.side_bar = self.ui.findChild(QWidget, "side_bar")
        self.toggle_button = self.ui.findChild(QPushButton, "toggle_button")

        # 初始化侧边栏的位置
        self.side_bar.setFixedWidth(200)
        self.side_bar.setVisible(False)

        # 连接按钮的点击事件
        self.toggle_button.clicked.connect(self.toggle_side_bar)

        # 初始化动画
        self.animation = QPropertyAnimation(self.side_bar, b"geometry")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)

        # 记录侧边栏的初始位置
        self.side_bar_initial_pos = QRect(0, 0, 200, self.height())

    def toggle_side_bar(self):
        if self.side_bar.isVisible():
            # 隐藏侧边栏
            start_geometry = self.side_bar.geometry()
            end_geometry = QRect(-200, start_geometry.y(), 200, start_geometry.height())
            self.animation.setStartValue(start_geometry)
            self.animation.setEndValue(end_geometry)
            self.side_bar.setVisible(False)
        else:
            # 显示侧边栏
            start_geometry = QRect(-200, self.side_bar.y(), 200, self.side_bar.height())
            end_geometry = self.side_bar_initial_pos
            self.animation.setStartValue(start_geometry)
            self.animation.setEndValue(end_geometry)
            self.side_bar.setVisible(True)

        self.animation.start()

    def resizeEvent(self, event):
        # 更新侧边栏的初始位置
        self.side_bar_initial_pos = QRect(0, 0, 200, self.height())
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())