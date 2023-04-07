import pymysql
import pandas as pd

# 建立连接
conn = pymysql.connect(
    user="root",
    password="123456",
    host="127.0.0.1",
    database="test",
    port=3306,
    charset="utf8mb4"
)

df = pd.read_sql("select * from people", conn)

print(df.items)
