# __author__: "Yu Dongyue"
# date: 2021/5/7
# 自定义过滤器
# 过滤器的本质就是python 的函数
from django import template

# 创建一个Library类的对象
# 添加此对象的filter
register = template.Library()


# 自定义的过滤器函数，至少有一个参数，最多有两个参数
@register.filter
def mod(num):
    """
    判断num是否未偶数
    :type num: int
    """
    return num % 2 == 0


@register.filter
def mod_val(num, val):
    return num % val == 0
