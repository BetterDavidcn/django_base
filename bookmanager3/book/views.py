from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo, PeopleInfo

# Create your views here.
def index(request):

    return HttpResponse('OK!')


def create_book(request):
    book = BookInfo.objects.create(
        name='函数加密',
        pub_date='2000-1-1',
        readcount=10
    )
    return HttpResponse('Create !')


def shop(request, a, b):
    query_params = request.GET
    print(query_params)
    order = query_params.get('order')
    print(order)
    return HttpResponse('hhh'+a+b+':'+query_params['order'])


def get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')