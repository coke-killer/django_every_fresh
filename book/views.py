from django.shortcuts import render
from book.models import *
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


# request 就是HttpRequest类型的实例对象，包含浏览器请求的信息

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


def area_se(request):
    # 获取哈尔滨市的上级地区和夏季地区
    pl = PlaceInfo.objects.get(p_title='哈尔滨市')
    # 查询上级地区 反向，，对象点关联属性
    parent = PlaceInfo.objects.filter(placeinfo__id=3).first()
    # parent=pl.placeinfo_set().all()
    # 查询夏季地区
    children = PlaceInfo.objects.filter(k__id=3)
    # children = pl.k
    return render(request, 'book/area.html', {'pl': pl, 'parent': parent, 'children': children})


def books(request):
    book = BookInfo.objects.filter(heroinfo__id=1)
    return HttpResponse(book)


def login_before(request):
    # 获取cookie  username
    if 'username' in request.COOKIES:
        # 获取记住的用户名
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, "book/login.html", {'username': username})


def login_check(request):
    # 1、 获取提交的用户名和密码
    # request.POST保存post方式提交的参数 QueryDict类型对象
    # request.GET保存get方式提交的参数 QueryDict 类型对象
    print(type(request.POST))
    name = request.POST.get('username')
    print(name)
    ps = request.POST.get('password')
    print(ps)
    remember = request.POST.get('remember')
    # 2、进行登录的校验
    # 3、返回应答
    if name == '123' and ps == '123':
        resp = HttpResponseRedirect('/book/index')
        if remember == 'on':
            # 设置cookie username 过期时间
            resp.set_cookie('username', name, max_age=7 * 24 * 3600)
        return resp

    else:
        return HttpResponseRedirect('/book/login')


def ajax_test(request):
    # 显示ajax页面
    return render(request, 'book/test_ajax.html')


def ajax_handle(request):
    # ajax请求处理
    # 返回json数据 {’res‘:1}
    return JsonResponse({'res': 1})


def login_ajax(request):
    # 显示ajax登录页面
    return render(request, 'book/loginajax.html')


def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == '123' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


def set_cookie(request):
    # 设置cookie信息
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息
    # response.set_cookie('num', 1)
    # 设置过期时间两周
    response.set_cookie('num', 1, max_age=14 * 24 * 3600)
    # response.set_cookie('num', 1, expires=datetime.now() + timedelta(days=14))
    # 返回一个response
    return response


def get_cookie(request):
    # 获取cookie信息
    num = request.COOKIES.get('num')
    return HttpResponse(num)
