# 创建并运行dockers
创建镜像
```shell
docker buildx build --platform linux/amd64 -t django_p:latest .
```

# 相关预计
新建项目
```shell
Django-admin startproject django
```
新建模块
```shell
python manage.py startapp db_mysql
```
创建新的迁移策略
```shell
python manage.py makemigrations db_mysql
```
使用migrate修改数据库模式
```shell
python manage.py migrate
```
探测数据库并生成映射类
```shell
python manage.py inspectdb > db_mysql/models.py
```