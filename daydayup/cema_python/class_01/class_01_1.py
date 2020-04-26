# -*- coding:utf-8 -*-
# @Time :2019/12/1 21:18
# @Author   :testcode_susu
# @Email    :363389871@qq.com
# @File :a.py
import keyword

print("hello world")
print("hello cema")
#package 用于组织某一类代码

#查看项目路径 copy path
# E:\VIP\code\cema_python  项目路径
# E:\VIP\code\cema_python\class_01\class_01_1.py  文件路径



# 注释符 # ''' """

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 
 'yield']
 '''
#标识符  第一个字符必须以字母或者下划线开头，其他必须字母数字下划线组成，关键字不能作为标识符

#查看当前版本的所有关键字
print(keyword.kwlist)

#注意缩进  通过缩进表示代码块，缩进空格数可变，但是同一代码块用相同的缩进，一般用tab进行缩进

str1="hello world"
print(str1)

if True:
    print("True")
else:
    print("FALSE")

# ********元组***************
tuple1=(1,'name',2,1.1)
print(tuple1)
# 创建空元组
tup2=()
print('空元组:',tup2)
# 创建一个元素的元组,后面加上逗号
tup3=(1,)
print('只有一个元素的元组:',type(tup3))
print('读取第二元素：',tuple1[1])
print(type(tuple1[1:-1]))

# 元组不可以修改只能进行拼接
# tuple1[-1]=5.1
# print(tuple1)
tup4=(5.1,)
tuple1_1=tuple1+tup4
print('修改后的元组：',tuple1_1)

print('复制元素：',tup4*4)

if 1 in tuple1:
    print('存在')
else:
    print('不存在')
for x in tuple1:
    print(x)

# 元组常见内置函数

print('返回元组的长度：',len(tuple1))
tup4=(1,2,3,4,5.89)
print('最大值：',max(tup4),' 最小值：',min(tup4))
list1=[1,2,3,4,5.89]
print('list转换为元组:',tuple(list1))

