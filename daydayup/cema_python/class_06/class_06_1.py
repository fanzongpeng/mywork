# -*- coding:utf-8 -*-
# @Time :2019/12/12 20:09
# @Author   :testcode_susu
# @Email    :2804555260@qq.com
# @File :class_06_1.py
# import time
# from time import sleep

from  time import *
# from clas_06_2 import add as add1
import clas_06_2
# from class_06.clas_06_2 import add

# 必需参数函数
import sys


def hello(name):
    print('hello ',name)

# 关键字参数函数
def hello1(name,classname):
    print('hello ',name,classname)

# 默认参数函数
def hello2(name,classname='testcode'):
    print('hello ',name,'来到',classname,'课堂')

hello('dfbbzyl')  #必需参数调用函数参数个数及先后顺序必需与声明参数一致
hello1('bbz','testcode')

# 通过关键字调用
hello1(classname='testcode',name='yxw')# 通过关键字调用

# 通过调用默认参数函数
hello2('noah chen')
hello2('noah chen','cema')

# 定义一个不定长参数,参数带*
def getstudentinfo(name,*valuetupe):
    print(name)
    print(valuetupe)

# 调用加*参数
getstudentinfo('pb','testcode',18,'zhongguo')
getstudentinfo('pb') #也可以未命名参数不设置值，相当设置空元组()

# 参数带两个星号**的参数以字典的形式导入

# 定义一个不定长参数,参数带**
def getstudentinfo2(name,**valuetupe):
    print(name)
    print(valuetupe)

# 调用参数带两个*
getstudentinfo2('Y',classname1='testcode',elseinfo=(18,'china'))


# 定义一个不定长参数函数，*单独出现
def getstudentinfo3(name,*,age):
    print(name)
    print(age)
def getstudentinfo4(name,*,age,adress):
    print(name)
    print(age)
    print(adress)
#调用*单独出现
getstudentinfo3('j',age=18)
getstudentinfo4('btzdqkfj',adress='china',age=18)

# 调用嵌套
def a():
    print('hello a!')

def b():
    print('hello b!')
    a()
b()

# 定义嵌套
print('定义嵌套')
def c():
    print('hello c')
    def d():
        print('hello d')
    def e():
        print('hello e')
    d()
    e()

c()

# 递归函数
# def a1():
#     print('hello a1')
#     b1()
#
# def b1():
#     print('hello b1')
#     a1()

# b1()   #  b1  a1  调用b1 、a1

#匿名函数定义
sum=lambda num1,num2,num3:num2+num1+num3
# 匿名函数调用
print(sum(1,2,3))
print(sum(1,2,5))

# 模块
# 模块类型
# time.sleep(3)  #调用通过import导入
# sleep(3)        #通过from..import导入

# sleep(3)
#
# print('33333')

print('调用其他模块')
# print(add1(1,2))
print(clas_06_2.add(1,2))
# print(clas_06_2.jianfa(30,20))

print(sys)

# ['E:\\VIP\\code\\cema_python\\class_06',
#  'E:\\VIP\\code\\cema_python',
#  'C:\\Python37\\python37.zip', 'C:\\Python37\\DLLs',
#  'C:\\Python37\\lib', 'C:\\Python37',
#  'E:\\VIP\\code\\cema_python\\venv', 'E:\\VIP\\code\\cema_python\\venv\\lib\\site-packages', 'E:\\VIP\\code\\cema_python\\venv\\lib\\site-packages\\setuptools-40.8.0-py3.7.egg', 'E:\\VIP\\code\\cema_python\\venv\\lib\\site-packages\\pip-19.0.3-py3.7.egg']
# ]


import class_05.class_05_1  # 当有包导入模块方式1
class_05.class_05_1.hello() # 调用模块

from class_05 import class_05_1  # 当有包导入模块 from 包名 import 模块名
class_05_1.hello()                 # 调用模块


from class_05.class_05_1 import hello  # 当有包导入模块 from 包名.模块名 import 函数名
hello()             # 调用模块



