from django.http import HttpResponse
from django.shortcuts import render
from django.db.models  import F, Q

from book.models import BookInfo, PersonInfo


# Create your views here.
def index(request):

    return HttpResponse('OK!')

#
# ########################################################################
# # 新增：方式1 save
# book = BookInfo(
#     name = 'Django',
#     pub_date = '2000-1-1',
#     read_count= 10
# )
#
# book.save()
#
# # 新增：方式2 .objects.create()
# BookInfo.objects.create(
#     name = 'Django2er2',
#     pub_date = '2000-1-1',
#     read_count= 10
# )
#
# ###########################################################################
# # 修改数据 方式1
# book = BookInfo.objects.get(id=1)
# book.name = 'new'
# book.save()
#
# # 修改数据 方式2
# BookInfo.objects.filter(id=1).update(name='asdawewreewrewrwe', comment_count=354)
#
# ###########################################################################
# # 删除数据：物理删除和逻辑删除
#
# book.delete()
# BookInfo.objects.filter(id=5).delete()
#
#
#
# ##################################查询#######################################3
# try:
#     BookInfo.objects.get(id=1)
# except:
#     print('查询结果不存在！')
#
# # 查询所有的
# BookInfo.objects.all()
#
#
# # count查询结果数量
# BookInfo.objects.count()
# BookInfo.objects.all().count()
#
#
# ####################################过滤查询#################################################
# filter(), exclude(), get()
#
# # 查询编号为1的图书 exact
# BookInfo.objects.get(id=1)
# BookInfo.objects.get(id__exact=1)
# BookInfo.objects.get(pk=1)
# BookInfo.objects.filter(id=1)
#
# # 查询书名包含'湖'的图书 contains
# BookInfo.objects.filter(name__contains='湖')
#
# # 查询书名以'部'结尾的图书 endswith, startswith
# BookInfo.objects.filter(name__endswith='部')
#
# # 查询书名为空的图书 isnull
# BookInfo.objects.filter(name__isnull=True)
#
# # 查询编号为1或3或5的图书 in
# BookInfo.objects.filter(id__in=[1, 2, 4])
#
# # 查询编号大于3的图书,比较查询 gt(greater than), gte(greater than equal), lt(less than), lte(less than equal)
# BookInfo.objects.filter(id__gt=3)
#
# # 不等于(和比较查询的结果相反)
# BookInfo.objects.exclude(id__gt=3)
#
# # 查询1980年发表的图书,日期查询year, month, day, week_day,hour,minute,second
# BookInfo.objects.filter(pub_date__month=10)
# BookInfo.objects.filter(pub_date__month__gt=1)
#
#
# # 查询1990年1月1日后发表的图书
# BookInfo.objects.filter(pub_date__gt='2000-1-1')
#
# #####################F对象#########################33
# # 查询阅读量大于等于评论量的图书
# BookInfo.objects.filter(read_count__gt=F('comment_count'))
#
# # 可以在F对象上使用算数运算
# BookInfo.objects.filter(read_count__lt=2*F('comment_count'))
#
#
# #########################Q对象#############################3
# # 查询阅读量大于20，并且编号小于3的图书
# BookInfo.objects.filter(read_count__gt=20, id__lt=3)
# BookInfo.objects.filter(read_count__gt=20).filter(id__lt=3)
#
# # Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或, 使用~操作符，表示非not
# BookInfo.objects.filter(Q(read_count__gt=20))
# BookInfo.objects.filter(Q(read_count__gt=20)|Q(read_count__lt=20))
#
# BookInfo.objects.filter(~Q(read_count__gt=20))