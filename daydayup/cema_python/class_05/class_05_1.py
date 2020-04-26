# -*- coding:utf-8 -*-
# @Time :2019/12/10 20:07
# @Author   :testcode_susu
# @Email    :2804555260@qq.com
# @File :class_05_1.py

# 实现求1加到100的和
i=1
sum=0
while i<=100:
    sum=sum+i
    print(i)
    i=i+1
print('实现求1加到100的和:',sum)

# while循环else语句
i=1
sum=0
while i<=100:
    sum=sum+i
    print(i)
    i=i+1
else:
    print('循环结束啦，返回求和的值:',sum)

# 实现求1加到100的和
sum=0
for x in range(1,101):
    sum=sum+x
print('for循环打印求和：',sum)

# 从0开始依次判断数字是否大于5，当大于五跳出循环
for i in range(0,5):
    print(i,'小于5')
else:
    print('循环结束')

# 依次编程字符串"hello",并打印出所有字符，当字符为l则跳出循环
print('依次编程字符串"hello",并打印出所有字符，当字符为l则跳出循环')
str1="hello"
for x in str1:
    if(x=='l'):
        break
    print(x)
print('循环结束啦')
str1="hello"
for x in str1:
    if(x=='l'):
        continue
    print(x)
print('循环结束啦')

str1="hello"
for x in str1:
    if(x=='l'):
        pass
    print(x)
print('循环结束啦')
# i=1
# while  i<10：
# #     循环体语句1
# #     for x in range(1,10)：
# #         循环体语句2
# #     # i+=1
# #     i=i+1
# 第一次外循环  i=1
#     内循环  重复执行循环9次
#
# 第二次外循环  i=2
# 内循环
#     重复执行循环9次
# 。。。。

# *
# **
# ***
# ****
# *****
print('打印如下图：')

for x in range(1,6):
    i=1
    while i<=x:
        print('*',end='')
        i+=1
    print()
# 逻辑：
# 1外循环打印空行  内循环 值打印*
# 2外循环打印空行  内循环  **

# 打印99乘法表打  经典面试题
print('打印99乘法表打  经典面试题')
for x in range(1,10):
    for y in range(1,x+1):
        print(str(y)+'x'+str(x)+'='+str(x*y),end='  ')
    print()

# 五参数无返回函数
def hello():
    print('hello testcode')

hello()#调用函数

def hello1():
    print('hello testcode')
    return 'hello testcode'

print('无参数有返回：')
print(hello1())

# 有参数无返回
def getinfo(name,classname):
    print('hello',name,'来到学院',classname)
    return
getinfo('bubizhui','testcode')
print(getinfo('bubizhui','testcode'))

# 有参数有返回
def getinfo1(name,classname):
    dict1={}
    dict1['name']=name
    dict1['classname']=classname
    return dict1
print('有参数有返回')
getinfo1('猪猪girl','testcode')
print(getinfo1('猪猪girl','testcode'))


def changenumber(a):
    a=10
b=2
changenumber(b)
print('参数传递是不可变数据类型,不受函数内部影响：',b)

def changelist(mylist):
    mylist.append([1,2,3,4])
    return mylist

print('参数传递是可变数据类型,受函数内部影响:')
mylist=[1,2,3,4,5,6,7]
changelist(mylist)
print(mylist)

# [1,2,3,4,5,6,7,[1,2,3,4]] 预期结果


