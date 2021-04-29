from django.contrib import admin
from book.models import *


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['b_title', 'b_pub_date', 'b_comment', 'b_read', 'is_delete']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['h_name', 'h_sex', 'h_comment', 'is_delete']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
