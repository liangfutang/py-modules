# 说明
实现对TDengine时序库的操作GUI

# 相关步骤
1. 打包
```shell
# --hidden-import PySide6.QtXml 参数是因为这个 QtXml库是动态导入，PyInstaller没法分析出来，需要我们告诉它，
pyinstaller demo1.py --onefile --noconsole --add-data="ui;ui" --strip --clean --hidden-import PySide6.QtXml
```