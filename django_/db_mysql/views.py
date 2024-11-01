from django.shortcuts import render, HttpResponse
from django.db import connection
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

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
@csrf_exempt
def orm_select(request):
    books = Book.objects.all()
    for book in books:
        print(f'(id:{book.id}, name:{book.name}, price:{book.price}, price:{book.create_time}, price:{book.update_time})')
    return HttpResponse("ok")

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer