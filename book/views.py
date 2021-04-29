from django.shortcuts import render
from book.models import *
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    books = BookInfo.objects.all()

    return render(request, 'book/index.html', {'books': books})


def insert(request):
    '''新增一本图书'''
    BookInfo(b_title='西游记', b_pub_date=datetime.now()).save()
    # return render(request, '', {})\
    # return HttpResponse('ok')
    # 重定向，完成两次响应，先是/book/insert 然后是/book/index
    return HttpResponseRedirect('/book/index')


def del_book(request, bid):
    BookInfo.objects.filter(id=bid).delete()
    return HttpResponseRedirect('/book/index')
