from django.db import models


# 设计和表对应的类
# Create your models here.
# 图书类
class BookInfo(models.Model):
    """
    图书模型类 ，在继承models模块中的Model对象之后
    """
    # 图书名称：CharFiled说明是一个字符串，max_length指定最大长度为20
    b_title = models.CharField(max_length=20)
    # 出版日期: 说明是一个日期类型
    b_pub_date = models.DateField()

    def __str__(self):
        return self.b_title


# 英雄任务类
class HeroInfo(models.Model):
    """
    和图书一对多
    """
    h_name = models.CharField(max_length=20)
    h_sex = models.BooleanField(default=False)
    h_comment = models.CharField(max_length=128)
    # 关系属性h_book建立图书和英雄类一对多关系
    h_book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    #
    def __str__(self):
        return self.h_name
