from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=32)
    pages = models.IntegerField()

    class Meta:
        db_table = 'book'
