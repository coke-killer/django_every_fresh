# Django

[简体中文](README.md) ∙ [英文](README.md)

## 安装及环境准备

基于`python3.9.4`与`Django3.2`

### 项目相关文件

`settings`: 数据库等的配置文件  
`__init__.py`一个空文件告诉项目说明  
`django_every_fresh`是一个`python`的包   
`urls` 是路由配置  
`wsgi.py` 一个兼容web项目的入口以便兼容web 项目  
`asgi.py` 一个兼容web项目的入口以便兼容web 项目  
`manage.py` 一个命令行工具，让各种项目和django进行交互   
新建项目时在终端执行：

```bash 
python manage.py startapp test
```

创建app

### ===============================================================

## 在django项目中一个功能模块用一个应用来实现

## app相关文件

在新创建的app python中的一些文件
`__init__.py`一个空文件告诉项目说明此app包是一个python的包
`models.py`写数据库相关的内容  
`test.py`写测试的代码  
`views.py` 定义处理函数也就是视图函数 处理每个请求
`admin.py` 就是和网站后台管理相关的，比如通过wab界面而不是通过sql语句的方式往数据库中添加字段 建立应用和项目之间的联系，需要
**对应用进行注册**  就是项目其实不知道应用本身存在 修改`setting`中的 `INSTALLED_APPS`

### MVC模式 核心思想就是解耦

M Model 模型与数据库进行交互  
V 视图 产生html页面  
C Controller,控制器 接受请求，与m和v进行交互，返回应答

### Django 开发的网站 MVT模式 遵循MVC类似思想，没有控制器

M model 模型 与数据库进行交互  
V view 视图 由视图模块接受数据  
T template 模板 和MVC中的V功能相同 由view进行参数接受然后处理然后利用model和数据库进行交互，通过template产生一个页面进行交互

### Django 自带 ORM框架 通过类和对象进行操作 也可以根据设计的类生成数据库中的表

O object 对象类  
R relations 关系数据库中的表  
M mapping 映射  
通过类和对象操作数据库和表，不需要写SQL语句

### 创建数据库表的两个步骤

- 生成迁移文件 命令
  ```bash
  python manage.py makemigrations
  ```
- 执行迁移生成表 命令
  ```bash
  python manage.py migrate
  ```
- 表名为应用名模型类名小写

### 通过admin.py后台管理页面操作数据表

- 语言和时区的本地化
    - 修改`setting`文件 的语言和时区
  ```python
  LANGUAGE_CODE = 'zh-hans'  # 使用中文
  TIME_ZONE = 'Asia/Shanghai'  # 中国时间
  ```
- 创建管理员(输入用户名和密码)
  ```bash
    - python manage.py createsuperuser
  ```
    - root root

- 注册模型类，告诉`Django`框架根据注册的模型类来生成对应管理页面，在`admin.py`中
- 自定义管理页面 控制显示哪些内容在页面上,需要在`admin.py`中自定义一个类，自定义显示的属性

```python
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
```

### 视图函数定义在view中，必须有一个参数request

- 定义app的urls配置文件，项目启动之后先找项目的urls的关联地址，然后在进入每个urls的关联地址进行匹配
  > [Django3.0path 配置教程](https://blog.csdn.net/u014535666/article/details/100668837)
  ```bash
    path('', include('testapp.urls')),  # 包含testapp中的urls文件
  ```

### 模板文件的使用

- 在工程下创建模板文件夹
- 配置模板目录
- 创建模板文件
    - 加载模板文件，将模板文件原有的内容都过来
      ```python
      from django.template import loader
      ``` 
    - 定义模板上下文，像模板文件传递数据
    - 模板渲染，得到一个标准的html内容

### model 模型类属性命名限制

- 不能是python保留字
- 不能出现__连续的下划线，由python查询方式决定
- 定义属性时需要指定字段类型，通过字段类型的参数指定选项
    - 属性名=models.字段类型(选项)
    - 字段类型定义在 django.db.models包中，字段类型如下：
        - `AutoField` 自动增长,通常不用指定,为id属性默认创建
        - `BooleanField` 布尔字段，值为True,或者False
        - `NullBooleanField` 支持Null,True,False 三种类型
        - `CharField(max length=最大长度)`字符串
        - `TextField` 文本字段，一般超过4000字
        - `IntegerField` 整数
        - `DecimalField(max_digits=None,decimal places=None) `十进制浮点是 ,max_digits表示总位，decimal_places表示小数位数，价格
        - ` FloatField` (浮点数，同上，精确度不同,比不上DecimalField)
        - `DateField([auto_now=False,auto_now_add=False])` 日期字段auto_now_add=True创建对象的时候自动赋值为当前时间，auto_now表示最后一次修改的时间戳
        - `DateTimeField` 日期时间同上
        - `FileField` 上传文件字段
        - `InmageField` 继承自FileField,对上传内容进行校验，确保是有效的图片
    - 通过选项实现对字段的约束
        - `default` 默认值,设置默认值
        - `primary key`主键，一般加上AutoField
        - `unique` 若为True,字段在表中必须有唯一值
        - `db_index` 若为True 自动在表中创建索引
        - `db_column` 字段的名称，如果未指定，则使用属性的名称
        - `null` 如果为True,表示允许为空，默认值是False
        - `blank` 如果为True，则该字段允许为空白，默认值是False
    - `default` 和 `blank` 不影响表结构，不用继续迁移

# ORM联合查询原则

### 通过模型类.objects属性可以调用如下函数

- get 返回表中满足条件且只能有一条的数据 如果有多条数据回抛出异常
- all 返回所有数据是一个QuerySet 查询集类型对象
- filter 条件格式 ，返回满足条件的数据
    - 模型类属性名__条件名=值  
      a) 判断相等 条件名：exact 查询编号为1 的图书 `BookInfo.objects.get(id=1)|BookInfo.objects.get(id__exact(1)|`    
      b) 模糊查询 查询书包含'传'的图书 `Bookinfo.objects.filter(b_title__contains('传'))`  查询书名以'部结尾'
      的图书 `BookInfo.objects.filter(b_title__endwith('部')`  
      c) 空查询 innull 查询书名不为空的图书 ```sql select * from book_bookinfo where b_title is not null```
      BookInfo.objects.filter(b_title__isnull=False)  
      d) 范围查询 id为1或者3或者5的图书 ```sql select * from book_bookinfo where id in (1,3,5)```对应的ORM方式为Boobinfo.objects.filter(
      b_id__in=[1,3,5])  
      e) 比较查询 gt ,gte, lt ,lte 查询id大于3的图书 ```sql select * from book_bookinfo where id >3``` Bookinfo.objects.filter(
      id__gt=3)  
      f) 日期查询 查询1980年发表的图书 Bookinfo.objects.filter(
      b_pub_date__year=1980)
      Bookinfo.objects.filter(
      b_pub_data__month=12) ```sql select * from book_bookinfo where b_pub_date between '1980-01-01' and '1980-12-31'```
      g) 查询出版日期大于1980年1月1日 Bookinfo.objects.filter(b_pub_date__gt=date(1980,1,1))
    - exclude 返回不满足条件的数据   
      a)Bookinfo.objects.exclude(id=3)
    - order by 排序   
      a) BookInfo.objects.all().order_by('id')  升序  
      b) BookInfo.objects.all().order_by('-id')  降序  
      c) 把id大于3的图书信息按阅读量从大到小排序显示 : BookInfo.objects.filter(id__gt=3).order_by('b_read')
    - Q 对象 作用：用于查询条件之间的逻辑关系。 not或者or ,可以对Q对象进行&|-操作。  `from django.db.models import Q`
      a) 查询id大于3或者阅读量大于30的图书信息 ：BookInfo.objects.filter(Q(id__gt=3)|Q(b_read__gt=30))
      b) 查询id大于3或者阅读量大于30的图书信息 ：BookInfo.objects.filter(Q(id__gt=3)&Q(b_read__gt=30))
      c) 查询id不等于3 的图书信息 ：BookInfo.objects.filter(~Q(id=3))
    - F 对象 用于类属性之间的比较   
      a)查询图书阅读量大于评论量的图书信息： BookInfo.objects.filter(b_read__gt=F('b_comment'))  
      b)查询图书阅读量大于2倍阅读量的叙述信息 BookInfo.objects.filter(b_read__gt=F('b_comment')*2)
    - 聚合函数 sum,avg,count,max,min aggregate函数   
      a) 查询所有图书的数目 ： BookInfo.objects.all().aggregate(Count('id'))   .all可以省略 BookInfo.objects.count()
      b) 所有图书阅读量的综合 ：BookInfo.objects.aggregate(Sum('b_read'))  
      c) 统计所有id大于3的所有图书的数目 BookInfo.objects.filter(id__gt=3).count()
    - 查询集 all,filter,exclude,order_by,aggregate 查询之后是一个QuerySet对象 可以继续调用这些函数  
      a) 惰性查询 ：只有再使用查询集里面护具的时候才会真正查询  
      b) 缓存：当使用同一个查询集的时候，第一次会查询，再次使用会使用缓存里面的结果。  
      c) 限制查询集进行切片，产生的是一个新的查询集，这个下标不允许为负值   
      d) 取出查询集第一条数据的两种方式 ： b[0] 不存在会抛出IndexError异常，b[0:1].get() 不存在抛出DoesNotExist异常，exists： 判断一个查询集是否有数据

# 模型类关系

- 一对多关系  
  a) 图书-英雄类 models.ForeignKey() 定义在多的类中
- 多对多关系  
  a) 新闻-新闻类型 体育信息 国际信息 定义在那个类中都可以 models.ManyToManyField()
- 一对一关系   
  a) 员工的基本信息-员工详细信息表 定义在哪个类中都可以 models.OneToOneField()

# 关联查询

- 一对多关联查询  
  a)  查询图书id为1的所有英雄的信息 一对多正向查询时：对象名字.多类名子小写_
  set()  `book=BookInfo.objects.get(id=1) book_heroinfo_set.all()` `HeroInfo.objects.filter(h_book__id=1)`
  b)  查询id为1的英雄的关联图书的信息
  一对多反向查询时：对象名字.单类关联属性()`hero=HeroInfo.objects.get(id=1) hero.h_book()` `BookInfo.objects.filter(heroinfo__id=1)`
- 通过模型类实现关联查询  
  a)  查询图书信息，要求图书中的英雄的描述包含‘八’  `BookInfo.objects.filter(heroinfo__h_comment__contents='八')`  相当于inner join b)
  b)  查询图书信息，要求图书中英雄id 大于 3 `BookInfo.objects,filter(heroinfo__id__gt=3)`  
  c)  查询书名为”天龙八部的“ 所有英雄  `HeroInfo.objects.filter(h_book__b_title='天龙八部')`  
  d)  
  

    



