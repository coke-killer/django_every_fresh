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







