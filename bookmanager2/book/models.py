from django.db import models

# Create your models here.
class BookConfig(models.Model):
    name = 'book'
    verbose_name = '书籍'