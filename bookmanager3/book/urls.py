from django.urls import path, converters
from django.urls import register_converter

from book.views import index, create_book, shop, get, register, post_json, method, response, set_cookie, get_cookie, \
    set_session, get_session, login, RegisterView, OrderView


# 定义转换器，并注册
class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        # 验证没问题的数据，给视图
        return int(value)

    def to_url(self, value):
        # 将匹配结果用于反向解析值
        return str(value)


register_converter(MobileConverter, 'phone')


urlpatterns = [
    path('index/', index),
    path('create/', create_book),

    # <转换器： 变量名>
    path('<int:id>/<phone:mobile>/', shop),
    path('get/', get),
    path('register/', register),
    path('json/', post_json),
    path('method/', method),
    path('response/', response),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('login/', login),
    path('new_login/', RegisterView.as_view()),
    path('order_info/', OrderView.as_view())
]
