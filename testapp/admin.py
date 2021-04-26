from django.contrib import admin
from testapp.models import *


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类,定义主页显示内容拍,值为类中定义的属性"""
    list_display = ["id", "b_title", "b_pub_date"]


# 自定义任务管理类
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "h_name", "h_sex", "h_comment", "h_book"]


# 后台管理和相关文件
# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
