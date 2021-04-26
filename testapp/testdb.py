# __author__: "Yu Dongyue"
# date: 2021/4/26
from django.http import HttpResponse
from testapp.models import HeroInfo
from testapp.models import BookInfo
import datetime


def insert_db(request):
    book_info = BookInfo(b_title="水浒传", b_pub_date=datetime.datetime(2021, 5, 26)).save()
    return HttpResponse("<p>数据添加成功</p>")


def select_db(request):
    response_5 = ""
    # select * from
    # response_1 = BookInfo.objects.all()
    # 相当于where
    # 获取单个对象
    response_3 = BookInfo.objects.get(id=2)
    # 限制的返回数据 相当于 offset0 limit 2;
    # response_4 = BookInfo.objects.order_by('b_title')[0:2]
    # 输出所有数据
    # for var in response_1:
    #     response_5 += var.b_title + ""
    return HttpResponse("<p>" + response_3.b_title + "" + "</p>")


def update_db(request):
    book_1 = BookInfo.objects.get(id=1)
    book_1.b_title = '三国演义'
    book_1.save()
    # 另一种方式
    # BookInfo.objects.filter(id=1).update(b_title='小王日记')
    # 修改所有
    # BookInfo.objects.all().update(b_title='可新日记')
    return HttpResponse("<p> 修改成功 </p>")


def delete_db(request):
    # 删除id=1的数据
    BookInfo.objects.get(id=1).delete()
    # 另一种方式
    # BookInfo.objects.filter(id=1).delete()
    # 删除所有数据
    # BookInfo.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")


def insert_book_and_hero(request):
    # 直接添加id
    # book_1 = BookInfo(1, "天龙十八部", datetime.datetime(2021, 4, 26)).save()
    # HeroInfo(h_name="乔峰", h_sex=False, h_comment="降龙十八掌", h_book_id=1).save()
    # 添加book属性
    # book_1 = BookInfo(b_title="西游记", b_pub_date=datetime.datetime.now()).save()
    HeroInfo(h_name="熏悟空", h_sex=False, h_comment="七十二变", h_book_id=6).save()
    return HttpResponse("<p>保存成功</p>")


def select_book_and_hero(request):
    # 一对一关系对项目.关联属性，对象点关联属性
    hero = HeroInfo.objects.get(id=2)
    book = hero.h_book
    # 一对多关系,对象.对应类型小写下划线set点all
    s = BookInfo.objects.get(id=1).heroinfo_set.all()
    print(s)
    print(BookInfo.objects.all())
    print(HeroInfo.objects.all())
    return HttpResponse("<p>" + hero.h_name + hero.h_comment + "</p>")
