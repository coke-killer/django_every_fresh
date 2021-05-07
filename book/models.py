from django.db import models


class BookInfoManager(models.Manager):
    # 1、子u该返回的结果集
    def all(self):
        # 1、 调用父类all方法
        # super(BookInfo.self).all()
        books = super().all()  # QuerySet
        # 2、对父类进行过滤
        books = books.filter(is_delete=False)
        return books

    # 2、封装函数：操作模型类对应的数据表包括增删改查的方法
    @staticmethod
    def create_book(self, b_title, b_pub_date, b_read, b_comment, is_delete):
        # 1、创建一个图书对象
        # 2、获取self所在的模型类，否则下一行获取模型类的方式需要使名字进行一一对应
        book = self.model()
        # book = BookInfo()
        book.b_title = b_title
        book.b_comment = b_comment
        book.b_read = b_read
        book.b_pub_date = b_pub_date
        book.is_delete = is_delete
        # 2、保存进数据库
        book.save()
        return book

    pass


# Create your models here.
# 数据库表名字 book_bookinfo
class BookInfo(models.Model):
    # 名称
    b_title = models.CharField(max_length=20)
    # 出版日期
    b_pub_date = models.DateField()
    # 阅读量
    b_read = models.IntegerField(default=0)
    # 评论量
    b_comment = models.IntegerField(default=0)
    # 删除标记
    is_delete = models.BooleanField(default=False)

    # book = models.Manager  # 自定义了一个models.Manager对象
    objects = BookInfoManager()  # 自定义一个BookInfoManager类的对象

    # @staticmethod
    # @classmethod
    # def create_book(cls, b_title, b_pub_date, b_read, b_comment, is_delete):
    #     # 1、创建对象
    #     book = cls(b_title=b_title, b_pub_date=b_pub_date, b_read=b_read, b_comment=b_comment, is_delete=is_delete)
    #     # 2、保存进数据库
    #     book.save()
    #     return book
    class Meta:
        db_table = 'bookinfo'  # 指定模型类对应的表名

    def __str__(self):
        return self.b_title


class HeroInfo(models.Model):
    h_name = models.CharField(max_length=20)
    h_sex = models.BooleanField(default=False)
    h_comment = models.CharField(max_length=200)
    is_delete = models.BooleanField(default=False)
    # 关系属性
    h_book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.h_name


#
#
# # 新闻类型类
# class NewsType(models.Model):
#     # 类别名
#     type_name = models.CharField(max_length=20)
#     # 关联属性，在这里或者下一个函数中
#     news_info = models.ManyToManyField('NewsInfo')
#
#
# class NewsInfo(models.Model):
#     title = models.CharField(max_length=128)
#     content = models.TextField
#     pub_date = models.DateTimeField(auto_now_add=True)
#     # 关系属性
#     # news_type = models.ManyToManyField('NewsType')
#
#
# class EmployBasicInfo(models.Model):
#     # 姓名
#     name = models.CharField(max_length=20)
#     # 年龄
#     age = models.IntegerField()
#
#     sex = models.BooleanField(default=False)
#     employ_detail_info = models.OneToOneField('EmployDetailInfo', on_delete=models.CASCADE)
#
#
# class EmployDetailInfo(models.Model):
#     addr = models.CharField(max_length=256)
# 关系属性
# employ_basic_info = models.OneToOneField('EmployBasicInfo')

class PlaceInfo(models.Model):
    p_title = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区,建立自关联
    k = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    # class Meta:
    #     db_table = 'areas'
