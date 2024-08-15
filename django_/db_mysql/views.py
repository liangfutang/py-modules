from django.shortcuts import render, HttpResponse
from django.db import connection
from .models import Book

# Create your views here.

# 使用原生方式查数据库表数据
def native_select(request):
    cursor = connection.cursor()
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return HttpResponse("ok")

# 使用orm方式查数据库表数据
def orm_select(request):
    books = Book.objects.all()
    for book in books:
        print(f'(id:{book.id}, name:{book.name}, pages:{book.pages})')
    return HttpResponse("ok")
