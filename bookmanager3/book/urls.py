from django.urls import path

from book.views import index, create_book, shop, get


urlpatterns = [
    path('index/', index),
    path('create/', create_book),
    path('<a>/<b>/', shop),
    path('get/', get)
]