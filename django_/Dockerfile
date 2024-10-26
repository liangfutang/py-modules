FROM python:3.12-slim
# 工作目录
WORKDIR /app
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir django==3.0.*
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]