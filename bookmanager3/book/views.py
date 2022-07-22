import json
import re

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
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


def shop(request, id, mobile):
    # if not re.match('\d{5}', b):
    #     return HttpResponse('NO')
    query_params = request.GET
    print(query_params)
    order = query_params.get('order')
    print(order)
    return HttpResponse('hhh')


def get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')


def register(request):
    data = request.POST
    print(data)
    return HttpResponse('OK'+data)


def post_json(request):
    body = request.body
    body = body.decode()
    body = json.loads(body)
    print(body)
    print(type(body))
    print(body['name'])
    print(request.META['SERVER_PORT'])
    return HttpResponse('OK'+str(body))


def method(request):
    print(request.method)
    print(request.user)
    print(request.path)
    print(request.FILES)
    print(request.method)
    return HttpResponse('OK')


def response(request):
    # response = HttpResponse()
    #
    # # 自定义响应头
    # response['MEMEXIEA'] = 'good'
    # response.status_code = 200
    # response.content = 'hhhhh'
    # return response

    # # JsonResponse
    # json_a = {
    #     'city': 'Beijing',
    #     'name': 'hhhhh'
    # }
    # mylist = [
    #     {
    #         'city': 'Beijing',
    #         'province': 'Beijing',
    #     },
    #     {
    #         'city': 'Shanghai',
    #         'province': 'Shanghai',
    #     }
    # ]
    # return JsonResponse(mylist, safe=False)

    # redirect重定向
    return redirect('https://www.baidu.com')
