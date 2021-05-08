# Django

[简体中文](README.md) ∙ [英文](README.md)

# 安装及环境准备

基于`python3.9.4`与`Django3.2`

# 项目相关文件

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

# MVC模式 核心思想就是解耦

M Model 模型与数据库进行交互  
V 视图 产生html页面  
C Controller,控制器 接受请求，与m和v进行交互，返回应答

# Django 开发的网站 MVT模式 遵循MVC类似思想，没有控制器

M model 模型 与数据库进行交互  
V view 视图 由视图模块接受数据  
T template 模板 和MVC中的V功能相同 由view进行参数接受然后处理然后利用model和数据库进行交互，通过template产生一个页面进行交互

# Django 自带 ORM框架 通过类和对象进行操作 也可以根据设计的类生成数据库中的表

O object 对象类  
R relations 关系数据库中的表  
M mapping 映射  
通过类和对象操作数据库和表，不需要写SQL语句

# 创建数据库表的两个步骤

- 生成迁移文件 命令
  ```bash
  python manage.py makemigrations
  ```
- 执行迁移生成表 命令
  ```bash
  python manage.py migrate
  ```
- 表名为应用名模型类名小写

# 通过admin.py后台管理页面操作数据表

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

# 视图函数定义在view中，必须有一个参数request

- 定义app的urls配置文件，项目启动之后先找项目的urls的关联地址，然后在进入每个urls的关联地址进行匹配
  > [Django3.0path 配置教程](https://blog.csdn.net/u014535666/article/details/100668837)
  ```bash
    path('', include('testapp.urls')),  # 包含testapp中的urls文件
  ```

# 模板文件的使用

- 在工程下创建模板文件夹
- 配置模板目录
- 创建模板文件
    - 加载模板文件，将模板文件原有的内容都过来
      ```python
      from django.template import loader
      ``` 
    - 定义模板上下文，像模板文件传递数据
    - 模板渲染，得到一个标准的html内容

# model 模型类属性命名限制

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

# 通过模型类.objects属性可以调用如下函数

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
- 通过模型类实现关联查询时:要查哪个表中的数据就需要通过哪个类来查 写关联查询条件的时候，如果类中没有关系属性条件需要写对应类的名字如果有关系属性则需要些关系属性  
  a)  查询图书信息，要求图书中的英雄的描述包含‘八’  `BookInfo.objects.filter(heroinfo__h_comment__contents='八')`  相当于inner join b)
  b)  查询图书信息，要求图书中英雄id 大于 3 `BookInfo.objects,filter(heroinfo__id__gt=3)`  
  c)  查询书名为”天龙八部的“ 所有英雄  `HeroInfo.objects.filter(h_book__b_title='天龙八部')`
- 自关联那是一种特殊的一对多关系
- 管理器 objects 是Django自动生成的models.Manger类的一个对象 每个类有一个这个对象 通过这个管理器可以实现对数据的查询 自定义管理器之后Django不再帮我们生成默认的objects管理器  
  a) 自定义一个管理器 ，这个类继承models.Manger类 再`BookInfo`类中定义 `book = models.Manager` 之后需要使用`Bookinfo.book.all()` 来查询  
  b) 目的： 改变查询的结果集  
  c) 封装增删改查函数，又使得model中的数据不变,可以将放在BookInfo中封装的函数放入BookInfoManager中。使用`self.model()`就可以创建一个跟自定义管理器对应的模型类对象
  ```python
    @classmethod
    def create_book(cls, b_title, b_pub_date, b_read, b_comment, is_delete):
        # 1、创建对象
        book = cls(b_title=b_title, b_pub_date=b_pub_date, b_read=b_read, b_comment=b_comment, is_delete=is_delete)
        # 2、保存进数据库
        book.save()
        return book
  ```
  ```python
    @staticmethod
    from book.models import BookInfo
    def create_book(b_title, b_pub_date, b_read, b_comment, is_delete):
        # 1、创建一个图书对象
        book = BookInfo()
        book.b_title = b_title
        book.b_comment = b_comment
        book.b_read = b_read
        book.b_pub_date = b_pub_date
        book.is_delete = is_delete
        # 2、保存进数据库
        book.save()
        return book
  ```
- 模型和管理器之间的关系

1. 模型类BookInfo继承自models.Model 通过`objects=BookInfoManager()`在`BookInfo`中创建对象
2. 模型管理器类BookInfoManager 继承自models.Manager  `self.model()`获取 `self` 所在模型类的类名

- 通过元选项指定数据库表名，使得数据库表明不依赖 app的名字

```python
class Meta:
    db_table = 'bookinfo' 
```

# 视图功能

- 视图功能： 接受请求，进行处理，与M和T进行交互，返回应答 返回HTML内容 HttpResponse,也可能重定向redirect
- 使用：
    1. 定义视图函数，request参数必须有，是一个HttpRequest类型的对象。参数名可以变化
    2. 配置url，建立url和视图函数之间的对应关系
- url 配置过程
    1. 在项目的url文件中包含具体应用的urls文件，在具体应用的urls文件中包含url和视图的对应关系
    2. url配置项是顶底在一个名字叫urlpatterns的列表中，其中每一个元素都是一个配置项，每一个配置项都调用url函数
- 视图错误
    + 404: 找不到页面，默认会显示一个标准的作物页面，如果要显示自定义页面，则需要在template目录下面自定义一个`404.html`文件
        + url每日有配置
        + url配置错误
    + 500服务端的错误
        + 代码出错
    + 网站开发完需要关闭调试，在settings.py文件中
        + debug=False
        + ALLOWED_HOST=['*']
- 捕获url参数  
  进行url匹配时，把所需要捕获的部分设置成一个正则表达式组，这样django框架就会自动把匹配成功后相应组的内容作为参数传递给视图函数
    + 位置参数： 位置参数，参数名可以随意指定`url=(r'^showarg(\d+)$',views.show_arg)`
    + 关键字参数： 在位置参数的基础上给正则表达式组命名即可。`url=(r'^showarg(?p<num>\d+)$',views.show_arg)`
    + ?p<组名> 组名和视图函数接收的参数名一致
    + 关键字参数，视图中参数名必须和正则表达式名一致
- HttpRequest参数
    + method 获取请求方式, get|post
    + path 一个字符串，表示请求的完整路径，不包括域名和参数部分
    + encoding 一个字符串，None表示提使用浏览器默认设置，一般为utf-8，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding
    + GET QueryDict类型对象。类似于字典，包含get请求方式的所有参数
    + POST QueryDict类型对象。类似于字典，包含post请求方式的所有参数
    + COOKIES 保存浏览器发送给服务器的cookie以键值对的形式
    + session
- *ajax 异步的javascript ，在不加载页面的情况加，对页面进行局部刷新。*
  ```ajax
  $.ajax({
    'url': 请求地址,
    'type':请求方式,
    'dataType':预期返回的数据格式,
    'data'：参数
  }).success(function(data){
    //回调函数
  })
  ```
- *cookie 由老板也就是服务器生成存储在浏览器的一小段文本信息*
    + 你(浏览器)->老板（服务器)->卖豆浆 老板记性不好记不住你买豆浆 ；你买完豆浆老板给你一个条（设置cookie），拿条换豆浆（读取cookie）你在过去就知道你买过豆浆了
    + 特点：比如买完烧饼又买的豆浆，此时之后把买豆浆的单子给老板，不会涉及到买烧饼的单子以键值对的形式存储，通过浏览器访问一个网站时，会将浏览器存储的跟网站相关的所有`cookie`
      信息发送给该网站的服务器,`request.COOKIES`
    + cookie是基于域名安全的 比如说访问百度设置一堆cookie，访问土豆网设置一堆cookie，那么访问百度的时候是不会携带土豆网的cookie过去的
    + 设置cookie 需要`HttpResponse`类的对象或者是它子类的对象`HttpResponseRedirect`和`JsonResponse` `set_cookie` 浏览器发送给服务器的`cookie`
      保存在`COOKIES`中
    + cookie 是有过期时间的，如果不指定， 默认关闭浏览器之后cookie就会过期
- *session 存储在服务器端*
    + 你->去办健身卡，你的信息（session）都保存在电脑(服务器)中，给你一个卡号（cookie sessionId），下一次只需要你的卡号，我就可以从我的电脑中找到你的信息
    + `--------------------------------------------`
    + session_key | session_data |
    + `--------------------------------------------`
    + 唯一标识码 | {'username':123,'age':10}|
    + `--------------------------------------------`
    + 返回应答，让浏览器保存这个唯一标识码也就是session_id
    + 在访问网站，服务器获取session_id,根据session_id的值取出对应的session的信息
    + 特点： 以键值对存储，依赖于cookie，是唯一的，唯一标识码保存在session_id cookie中，也是有过期时间的
    + 设置`session` `request.session['username']='xiaowang'`  `request.setsession='''`
    + 设置`session` 的过期时间 `request.session.set_expiry(5)` 秒数，0关闭浏览器过期，None,默认两周
    + 使用`session`可以记住用户的登录状态 ,登录之后设置一个session.只要有这个session就说明是登陆过了

# `cookie` 和 `session` 使用场景

+ `cookie` 记住用户名，安全性要求不高，保存再浏览器端
+ `session` 涉及到安全性要求比较高的数据。银行卡账号，密码，保存在服务器端

# 模板文件不仅仅是html好包含下面两个内容

+ 静态内容 `css、js、html`
+ 动态内容： 用于动态去产生一些网页内容，通过模板语言来产生

# 模板文件的使用

+ 通常是在视图函数中使用模板产生`html`内容返回给客户端
    + 加载模板文件 `loder.get_template` 获取模板文件的内容，产生一个模板对象
    + 定义模板上下文`RequestContext` 给模板文件传递数据
    + 模板渲染产生`html` 页面内容 `render` 用传递的数据替换相应的变量，产生一个替换后的标砖的`html`内容

# 模板文件加载顺序

+ 首先先去配置的模板目录下面招模板（html）文件
+ 去installed_apps下面的每个应用去找模板文件，前提是应用中必须有templates文件夹

# 模板语言

+ 模板语言简称未`DTL` `Django Template Language`

# 模板变量 全部通过点进行获取

+ 模板变量有数字、字母、下划线和点组成，*不能以下划线开头*，使用模板变量：{{模板变量名}}
+ 模板变量的解释顺序：
    + 例如`{{book.b_title}}`  
      a) 首先把book当成一个字典，把`b_title`当成键名，进行取值，`book['b_title']`  
      b) 把book当成一个对象，把`b_title`当成属性，进行取值`book.b_title`  
      c) 把book当成一个对象，把`b_title`当成对象的方法，进行取值`book.b_title`
    + 例如`{{book.0}}`  
      a) 首先把book当成一个字典，把0当成键名，进行取值`book['0']`  
      b) 把book当成一个列表，把0当成下表，进行取值`book[0]`
    + 如果解析失败，则产生内容时用空字符串填充模板变量
    + 使用模板变量时：前面的可能是一个 字典、一个对象或者是一个列表

# 模板标签

+ 循环 `{%if%} {%end if%}`
+ 条件判断
+ 过滤器 改变日期显示格式 格式： 模板变量|过滤器：参数 `{{ book.b_pub_date | date:'Y年-M月-d日'}}`
+ [模板标签和内置过滤器参考资料](https://blog.csdn.net/lengfengyuyu/article/details/83342639)

# 模板继承

+ 享有共同的部分减少代码复用 可获取父亲block中的内容一起显示，也可以不获取内容直接在子模板中进行重写

# html转义

+ 转义显示标签，不转义显示html样式

# 装饰器 类似于aop,定义在方法执行之前运行那些函数

# csrf攻击 跨站请求伪造 Django默认启用了csrf防护,只针对POST方式的提交

首先做一个登录页，让用户输入用户名和密码进行登录，登陆成功之后调换到修改密码页面。在修改密码页面输入新密码，点击确认按钮，完成密码修改 登录页需要一个`login.html`,修改密码需要一个`change_pwd.html`
在进行网站开发的时候，有些网站是用户登录之后才能访问的，加入用户访问了这个地址，需要进行登录判断，如果用户登录了的话可以进行后续的登录，如果没有登录需要跳转到登录页

+ 登录正常网站之后，你的浏览器保存了session_id，并且没有退出
+ 不小心访问了另外一个网站并且点击了页面上面的按钮
+ 因为无法获取隐藏域中的信息所以就认为是安全

# 验证码

为了防止暴力请求，可以加入验证码功能，如果验证码错误则不需要处理，可以减少业务服务器、数据服务器的压力

# 反向解析

+ 根据url正则表达式的配置动态的生成url
+ 在项目的urls配置中指定namespace
+ 在app的url中指定name
+ 在app的url 的 urlpatterns上方加入app_name = '[book]'