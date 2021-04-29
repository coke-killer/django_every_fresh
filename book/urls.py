# __author__: "Yu Dongyue"
# date: 2021/4/27
from django.urls import path
from book import views

urlpatterns = [
    path('book/index', views.index),
    path('book/insert', views.insert),
    path('book/delete/<int:bid>', views.del_book),
]
