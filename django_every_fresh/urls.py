"""django_every_fresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from testapp import views
from testapp import testdb
from testapp import views

# 项目的path地址
urlpatterns = [
    path('admin/', admin.site.urls),  # 配置项目
    path('insert/', testdb.insert_db),
    path('select/', testdb.select_db),
    path('update/', testdb.update_db),
    path('delete/', testdb.delete_db),
    path('insertbookandhero', testdb.insert_book_and_hero),
    path('selectbookandhero', testdb.select_book_and_hero),
    path('index', views.index),
    path('', include('testapp.urls')),  # 包含testapp中的urls文件
    path('', include('book.urls', namespace='book1')),
]
