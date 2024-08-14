from django.shortcuts import render, HttpResponse
from django.db import connection

# Create your views here.

# 使用原生方式查数据库表数据
def select_book(request):
    cursor = connection.cursor()
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return HttpResponse("ok")
