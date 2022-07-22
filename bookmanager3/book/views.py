import json
import re

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View

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


def set_cookie(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    response = HttpResponse('OK')
    response.set_cookie('name', username, max_age= 3600)
    response.set_cookie('password', password)

    return response


def get_cookie(request):
    # print(request.COOKIES)
    name = request.COOKIES
    response = HttpResponse('OK')
    response.delete_cookie('name')
    return response


def set_session(request):
    user_id = 1
    user_name = request.GET.get('user_name')
    request.session['user_id'] = user_id
    request.session['user_name'] = user_name

    # # clear  和 flush
    # request.session.clear()
    # request.session.flush()
    request.session.set_expiry(3600)

    return HttpResponse('OK')


def get_session(request):
    # user_id = request.session['user_id']
    # user_name = request.session['user_name']
    # get默认为None
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    content = '{}:{}'.format(user_id, user_name)
    return HttpResponse(content)


def login(request):
    if request.method == 'GET':
        return HttpResponse('get')
    else:
        return HttpResponse('post')


class RegisterView(View):

    def get(self, requst):

        return HttpResponse('GET')

    def post(self, request):

        return HttpResponse('Post')


class Person:

    def play(self):
        pass

    @classmethod
    def say(cls):
        pass

    @staticmethod
    def eat():
        pass
