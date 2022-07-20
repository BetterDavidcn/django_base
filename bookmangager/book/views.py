from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': 'ceshi 测试'
    }
    return render(request, 'book/index.html', context=context)