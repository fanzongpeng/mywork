# -*- coding:utf-8 -*-
# @Time :2019/12/3 20:05
# @Author   :testcode_susu
# @Email    :363389871@qq.com
# @File :class_02_1.py

import math
import random
print("hello world");print("hello cema")
str1="aaaaabbbbbb"+\
    "cccccddddd"
print(str1)
str2='''aaaaabbbbbb
    cccccddddd'''
print(str2)
str3=str1+\
    str2
print(str3)

# 空行主要用于代码维护和重构 比如函数之间，函数与类之间用空行，通过空行区别某一功能或含义代码

#代码组：具有相同缩进的代码叫代码组
# 子句：比如if/for/def/class以冒号结束及后面代码组，我们称作子句

if True:
    print("True")
else:
    print("False")


# print()函数自动换行，并可以支持多个参数
print("hello world")
print("hello cema","hello susu","123232")
# 不换行打印
print("hello world",end="")
print("hello cema","hello susu","123232")

#导包表示方式有哪些
# 1）from 模块 import 函数
# from keyword import kwlist,iskeyword
# print(kwlist)
# print(iword('True'))skey

# 2）import 模块
import keyword
# print('1111')=
# print(keyword.kwlist)

# 3）from 模块 import *
# from keyword import *
# print(kwlist)
# # print(iword('True'))skey


var1=4
var2=1
var3='1'
print(type(var1))
print(type(var3))
print(isinstance(var3,int))
print(type(var2))

var4=complex(1,1.1)
print(var4,var4.real,var4.imag,var4.conjugate())

# 数字类型进行运算（+ - * / //  ** ）

print(var1+var2,var1*var2)
print(var1/var2)  # /返回的是float
# 返回整型
print(type(var1//var2))

print(4//2.0)
print(4.0//2)
print(8//3)  #向下取整数
print(8/3)

print(type(int(2.0)))
print(abs(-2))
print(math.floor(4.5))
print(math.ceil(4.1))
# 保留几位小数，进行四舍五入 round(数字,n)n保留N小数
f=49.887
print(round(f,2))
print(round(f,0))
print(round(44.88,-1))

#返回随机数0~1实数random.random()
print(random.random())
#随机返回某个范围整数
print(random.randint(1,100))


#string类型
str1="hello world"
str2='hello cema'
str3='''
hello susu
hello xuzhu
'''
print(type(str1),type(str2),type(str3))
# 如何访问字符串中的子串
print(str1[0:5])
#截取str1从开始截取到倒数第二个字符
print(str1[0:-1])
# 截取str1从第二个字符截取到最后
print(str1[1:])
#截取整个字符
print(str1[:])
print(str1[::1])
#翻转字符串str1
print(str1[::-1])


str1="hello world"
str1=str1[0:6]+'cema'
print(str1)
print(str1*2)
if 'h' not in str1:
    print("存在")
else:
    print("不存在")

# hello\nworld
str4="hello\nworld"
str5="hello\000world"
str6="hell\tworld"
print(str6)
print("hello\\nworld")
print(r"hello\nworld")
print(R"hello\nworld")

print(" %s工作年限 %d 年"%('susu',11))
# str.format()
print(" {1}工作年限 {0} 年".format(11,'susu','1212321'))
list1=keyword.kwlist

print("当前版本的关键字有哪些：{0[0]}，{0[1]}".format(list1))
print(list1[0],list1[1])


print(list1)
str7=' '.join(list1)
print(str7)
print(type(str7))

str8="Hello world"
list2=str8.split(' ')
print(list2)

print(str8.find("aaaaa",0,len(str8)))
# print(str8.index("aaaaa",0,len(str8)))

print(str8.startswith('lll',0,len(str8)))

print(str8.strip(),str8.capitalize(),str8.upper(),str8.lower())
print(str8.count('l',0,len(str8)))













