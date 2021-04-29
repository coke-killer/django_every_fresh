from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from testapp.models import *


# Create your views here.
# 定义视图函数,HttpRequest
# 进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    # 进行处理,利用M和T进行交互
    # 使用模板文件,路径相对于templates
    # 1、加载模板文件，模板对象
    # temp = loader.get_template('testapp/index.html')
    # 2、定义模板上下文：给模板传递数据
    # context = RequestContext(request, {})
    # 3、模板渲染：产生标准的html内容并返回
    # res_html = temp.render(context)
    # 4、返回给浏览器
    # return HttpResponse(res_html)
    return render(request, "testapp/index.html", {"name": 123, "list": [1, 2, 3, 4, 5, 6, 7, 8]})


def index_2(request):
    return HttpResponse("hello python")


def show_books(request):
    """显示图书信息"""
    # 通过m查找图书表中的数据
    books = BookInfo.objects.all()
    return render(request, "testapp/show_books.html", {"books": books})


def show_books_detail(request, bid):
    """查询图书关联的英雄信息"""
    book = BookInfo.objects.get(id=bid)
    heroes = book.heroinfo_set.all()
    return render(request, "testapp/detail.html", {'book': book, 'heroes': heroes})
