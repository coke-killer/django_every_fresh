# __author__: "Yu Dongyue"
# date: 2021/4/26
from django.conf.urls import url
from django.urls import path
from testapp import views

urlpatterns = [
    # 通过url函数设置url路由配置项
    path('index', views.index),
    path('index2', views.index_2),

]
