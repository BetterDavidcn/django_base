from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='书籍')
    pub_date= models.DateField(null=True, verbose_name='发布日期')
    read_count = models.IntegerField(default=0, verbose_name='阅读人数')
    comment_count = models.IntegerField(default=0, verbose_name='评论条数')
    is_delete = models.BooleanField(default=False, verbose_name='已被删除')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'

    def __str__(self):
        return self.name

class PersonInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICE = (
        (0, 'unknown'),
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=20, unique=True, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0, verbose_name='性别')
    description = models.CharField(max_length=100, null=True, verbose_name='描述')
    is_delete = models.BooleanField(default=False, verbose_name='已被删除')

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='书籍')

    class Meta:
        db_table = 'personinfo'
        verbose_name = '人物信息'


    def __str__(self):
        return self.name


