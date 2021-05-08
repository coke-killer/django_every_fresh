# __author__: "Yu Dongyue"
# date: 2021/4/27
from django.urls import path
from book import views

app_name = '[book]'
urlpatterns = [
    path('book/index', views.index, name='index'),
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
    path('book/temp_inherit', views.temp_inherit),
    path('book/html_escape', views.html_escape),
    path('book/login_two_before', views.login_two_before),
    path('book/login_two_check', views.login_two_check),
    path('book/change_pwd', views.change_pwd),
    path('book/change_pwd_action', views.change_pwd_action),
    path('book/url_reverse', views.url_reverse),
]
