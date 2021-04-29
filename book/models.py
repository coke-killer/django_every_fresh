from django.db import models


# Create your models here.
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


# 新闻类型类
class NewsType(models.Model):
    # 类别名
    type_name = models.CharField(max_length=20)
    # 关联属性，在这里或者下一个函数中
    news_info = models.ManyToManyField('NewsInfo')


class NewsInfo(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField
    pub_date = models.DateTimeField(auto_now_add=True)
    # 关系属性
    # news_type = models.ManyToManyField('NewsType')


class EmployBasicInfo(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 年龄
    age = models.IntegerField()

    sex = models.BooleanField(default=False)
    employ_detail_info = models.OneToOneField('EmployDetailInfo', on_delete=models.CASCADE)


class EmployDetailInfo(models.Model):
    addr = models.CharField(max_length=256)
    # 关系属性
    # employ_basic_info = models.OneToOneField('EmployBasicInfo')
