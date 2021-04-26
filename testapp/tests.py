from django.test import TestCase


# Create your tests here.
class Student(object):
    age = 10


if __name__ == '__main__':
    s = Student()
    print(Student.objects)
