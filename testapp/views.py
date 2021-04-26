from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext


# Create your views here.
# 定义视图函数,HttpRequest
# 进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    # 进行处理,利用M和T进行交互
    # 使用模板文件,路径相对于templates
    # 1、加载模板文件，模板对象
    # 2、定义模板上下文：给模板传递数据
    # 3、模板渲染：产生标准的html内容并返回
    #4、返回给浏览器
    # return HttpResponse(temp.render(RequestContext(request, {'name': 'hello django'})))
    return render(request, "testapp/index.html", {"name": 123})


def index_2(request):
    return HttpResponse("hello python ")
