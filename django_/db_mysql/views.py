from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
import utils.results as results

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

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return JsonResponse({
            "status": 200,
            "data": serializer.data
        }, safe=False)

    def post(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return results.success(data=serializer.data)

    def put(self, request, *args, **kwargs):
        print("这是一个put方法")
        message = {"status": 200}
        return JsonResponse(message, safe=False)

    def delete(self, request, *args, **kwargs):
        message = {"status": 200}
        return JsonResponse(message, safe=False)