from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """
    继承Model，继承内置的增删改除等函数，系统自己添加主键，无需额外设置

    """
    # 创建字段
    name = models.CharField(max_length=100)

    # 以字符串格式显示
    def __str__(self):
        return self.name

class PersonInfo(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BooleanField()

    # 创建外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    # 以字符串格式显示
    def __str__(self):
        return self.name


