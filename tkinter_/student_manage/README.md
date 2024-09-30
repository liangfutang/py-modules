# 扫描当前项目中的所有依赖
## 安装第三方包
```shell
pip install pipreqs
```
## 生成requirements.txt
```shell
pipreqs ./ --encoding=utf-8 --force
```


# 生成虚拟环境
```shell
python -m venv venv
```

# 安装项目必须的依赖
```shell
pip install -r requirements.txt
pip install pyinstaller
```

# 建立虚拟环境
```shell
pipenv install
```
# 进入虚拟环境
```shell
pipenv shell
```

# 生成可执行文件
```shell
pyinstaller --onefile --noconsole --add-data="templates;templates"  main.py
```

# 删除虚拟环境
```shell
pipenv --clear
pipenv --rm
rm Pipfile 
rm Pipfile.lock
```
