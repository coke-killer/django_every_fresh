# __author__: "Yu Dongyue"
# date: 2021/4/27
from django.urls import path
from book import views

urlpatterns = [
    path('book/index', views.index),
    path('book/insert', views.insert),
    path('book/delete/<int:bid>', views.del_book),
    path('area/arease', views.area_se),
    path('book/books', views.books),
    path('book/login', views.login_before),
    path('book/login_check', views.login_check),
    path('book/ajax_test', views.ajax_test),
    path('book/ajax_handle', views.ajax_handle),
    path('book/login_ajax', views.login_ajax),
    path('book/login_ajax_check', views.login_ajax_check),
    path('book/set_cookie', views.set_cookie),  # 设置cookie
    path('book/get_cookie', views.get_cookie),
    path('book/set_session', views.set_session),
    path('book/get_session', views.get_session),
    path('book/clear_session', views.clear_session),
    path('book/index2', views.index_two),
    path('book/temp_var', views.temp_var),
    path('book/temp_tags', views.temp_tags),
]
