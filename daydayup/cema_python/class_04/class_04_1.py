# -*- coding:utf-8 -*-
# @Time :2019/12/8 20:59
# @Author   :testcode_susu
# @Email    :2804555260@qq.com
# @File :class_04_1.py
# a=10
a=10
if a>5 or a>10:
    print(a)
else:
    print('不打印a的值')
a=1
if not a:
    print(a)
else:
    print('不打印')
a=3
b=4
# 二进制  a  二进制  11    b 100
print('a&b:',a&b)
print('a|b:',a|b)
print('a^b:',a^b)
print('~b',~b)
print('a>>2:',a>>2)
print('a<<2：',a<<2)

a=10
b=20
if a is b:
    print('是引用相同标识')
else:
    print('不是相同标识')

if id(a)==id(b):
    print('是引用相同标识')
    print(id(a),id(b))
else:
    print('不是相同标识')

a,b,c,d=10,60,30,40
print(a+b/c*d)   # 10+((60/30)*40)
print(a+((b/c)*d))

# username=input('请输入用户：')
# password=input('请输入密码：')
# # 判断输入用户名和密码是否都是为admin，如果是打印登录成功，否则打印登录失败
# if username=='admin'and password=='admin':
#     print('登录成功')
# else:
#     print('登录失败')

# 多重if
# 成绩小于60不及格，>=85 优    小于85并且 >=75  中  >=60 and <75 为一般
# score=int(input('请输入成绩：'))
# if score<60:
#     print('不及格')
# elif score>=85:
#     print('优秀')
#
# elif score>=75 :
#     print('中等')
# else:
#     print('一般')


# if嵌套
# 成绩小于60不及格，>=85 优    小于85并且 >=75  中  >=60 and <75 为一般
score=80
if score>60:
    print('及格')
    if score>=85:
        print('优秀')
    elif score>=75:
        print('中等')
    else:
        print('一般')
else:
    print('不及格')
