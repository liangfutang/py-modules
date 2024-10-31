FROM python:3.12-slim
# 工作目录
WORKDIR /app
COPY . /app
# 设置环境变量
ENV PATH /usr/local/bin:$PATH
# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt
# 安装uWSGI
RUN pip install uwsgi

EXPOSE 8000
CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]