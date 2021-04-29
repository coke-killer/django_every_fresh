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
