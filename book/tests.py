from django.test import TestCase
import re

# Create your tests here.
# 从字符串str中找出数字
str = "123"
print(re.match(r'[0-9]+', str, flags=0).group(0))
