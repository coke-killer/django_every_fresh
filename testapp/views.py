from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 定义视图函数,HttpRequest
# 进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    # 进行处理,利用M和T进行交互
    return HttpResponse("老铁没毛病")
