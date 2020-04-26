# -*- coding:utf-8 -*-
# @Time :2019/12/6 17:16
# @Author   :testcode_susu
# @Email    :2804555260@qq.com
# @File :class_02_task.py

# 1、用print函数打印多个值
print('1、用print函数打印多个值：','hello cema','hello susu',1)
# 2、用print函数不换行打印
print('2、用print函数不换行打印:',end='')
print('hello cema',end='')
# 3、导入模块的方式有哪些
#     1)import 模块')
#     2)from 模块 import 函数1,函数2')
#     3)from 模块 import *'
# 4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
# 六种,number、string、tuple这三种为不可变类型，list、dict、set为可变类型
# 5、python3中可以支持哪些数值类型？
# int、bool、float、complex
# 6、判断变量类型有哪些方式，分别可以用哪些函数？
# type()
# isinstance()
# 7、分别对49 .698

# 作如下打印
# 1）四舍五入，保留两位小数
print(' 1）四舍五入，保留两位小数',round(49.698,2))
# 2）向上入取整
import math
print(' 2）向上入取整:',math.ceil(49.6982))
# 3）向下舍取整
import math
print(' 3）向下舍取整:',math.floor(49.6982))
# 4）计算8除以5返回整型
print(' 4）计算8除以5返回整型',8//5)
# 5）求4的2次幂
print(' 5）求4的2次幂',4**2)
# 6）返回一个（1, 100）随机整数
import random
print(' 6）返回一个（1, 100）随机整数:',random.randint(1,100))
# 8、依次对变量a, b, c赋值为1, 2, 3
a,b,c=1,2,3
# 9、截取某字符串中从2索引位置到最后的字符子串
str2='hello world'
print()
# 10、对字符串“testcode”做如下处理：
print('10、对字符串“testcode”做如下处理：')
str1='testcode'
#
# 1）翻转字符串
print(' 1）翻转字符串:',str1[::-1])
# 2）首字母大写
print(' 2）首字母大写:',str1.capitalize())
# 3）查找是否包含code子串，并返回索引值
print(' 3）查找是否包含code子串，并返回索引值',str1.find('code',0,len(str1)))
# 4）判断字符串的长度
print(' 4）判断字符串的长度',len(str1))
# 5）从头部截取4个长度字符串
print(' 5）从头部截取4个长度字符串:',str1[0:4])
# 6）把code替换为123
print(' 6）把code替换为123:',str1.replace('code','123'))
# 7）把“test code”字符串中的两个单词转换为列表中的元素，并打印处理
str1='test code'
print(' 7）把“test code”字符串中的两个单词转换为列表中的元素，并打印处理:',str1.split(' '))
# 8）把['test', 'code']把list变量中的元素连接起来
list1=['test', 'code']
print(" 8）把['test', 'code']把list变量中的元素连接起来:",''.join(list1))
# 11、如何打印出字符串“test\ncode”
print(R'11、如何打印出字符串“test\ncode”:',r'test\ncode')
# 12、如何创建一个空元组
tup1=()
print('12、如何创建一个空元组:',tup1)
# 13、创建一个只包含元素1的元组，并打印出该变量的类型
tup1=(1,)
print('13、建一个只包含元素1的元组，并打印出该变量的类型：',type(tup1))
# 14、元组中元素可以修改？如何更新元组中的元素？
print('14:元组为不可变数据类型，可以通过拼接更新元组')
# 15、对元组（1, 2, 3, 4, 5)做如下操作：
print('15、对元组（1, 2, 3, 4, 5)做如下操作：')
# 1）取倒数第二个元素
tup1=(1, 2, 3, 4, 5)
print(' 15-1:取倒数第二个元素:',tup1[-2])
# 2）截取前三个元组元素
print(' 15-2:截取前三个元组元素:',tup1[0:3])
# 3）依次打印出元组中所有元素
print(' 15-2:依次打印出元组中所有元素:')
for x in tup1:
    print('      ',x)
# 16、把元组(1, 2, 3, 4, 5, 6)元素格式化成字符串
print('16、把元组(1, 2, 3, 4, 5, 6)元素格式化成字符串：')
tup1=(1, 2, 3, 4, 5, 6)
print('{}'.format(tup1))

