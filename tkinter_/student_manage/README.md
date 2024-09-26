# 生成虚拟环境
```shell
python -m venv venv
```
# 生成requirements.txt
```shell
pip freeze > requirements.txt
```
# 生成可执行文件
```shell
pyinstaller --onefile --noconsole  main.py
```
