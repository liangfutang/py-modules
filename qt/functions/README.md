# 说明
本模块用作pyside2相关功能验证。python3.11不能安装pyside2，可以安装pyside66，只能使用python3.10或者能早版本安装pyside2

# 相关操作
1.1 当前文件夹打包
```shell
# --hidden-import PySide6.QtXml 参数是因为这个 QtXml库是动态导入，PyInstaller没法分析出来，需要我们告诉它，
pyinstaller demo1.py --onefile --noconsole --add-data="ui;ui" --strip --clean --hidden-import PySide6.QtXml
```
1.2 pressure打包
```shell
pyinstaller ./presure/main.py --onefile --noconsole --add-data="./presure/libs;libs" --add-data="./presure/images;images" --add-data="./presure/home.ui;home.ui" --add-data="./presure/login.ui;login.ui" --add-data="./presure/createTask.ui;createTask.ui" --clean
```

2. ui转python
```shell
pyside2-uic ./ui/stats.ui -o ./ui/output_file.py -e UTF-8
```