# -*- coding:utf-8 -*-
# @Time :2019/12/17 20:08
# @Author   :testcode_susu
# @Email    :2804555260@qq.com
# @File :class_08_1.py
# import calendar
# import time
#
# # 取得时间戳
# print(time.time())
#
# print(time.localtime())#获取当前时间元组
#
# print(time.asctime(time.localtime()))  #获取英文时间
#
# print('把时间转为时间戳：',time.mktime(time.localtime()))  #把时间转为时间戳
#
# print('把时间戳转换为时间元组：',time.localtime(1576584902.0))
#
# print('把时间转换为字符串：',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),type(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
#
# print(time.strftime('%Y-%m-%d',time.localtime()))
# print(time.strftime('%Y',time.localtime()))
#
# str1='2018-12-20 12:30:30'
# print('字符串转换为时间元组：',time.strptime(str1,'%Y-%m-%d %H:%M:%S')) #字符串转换为时间元组
#
#
# # 截取时间中部分信息
# print(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday,time.localtime().tm_hour)
# print(time.localtime().tm_min,time.localtime().tm_sec,time.localtime().tm_wday,time.localtime().tm_isdst)
# # 星期一到星期天（0~6）
#
#
# # ***********datetime模块***************
# import datetime
# #
# # # 如何用datetime表示元组
# dt=datetime.datetime(2018,12,17,20,38,30)
# print('用datetime创建时间元组：',dt)  #用datetime创建时间元组：
#
# # 获取当前时间
# print(datetime.datetime.now())
# print(datetime.datetime.today())
#
#
# print('获取指定时间时间戳:',dt.timestamp())  #获取指定时间时间戳
# print(datetime.datetime.now().timestamp())
#
# print('时间戳转换为时间元组：',datetime.datetime.fromtimestamp(1545050310.0))
#
# print('时间转换为字符串:',datetime.datetime.strftime(dt,'%Y-%m-%d'))
# print('字符串转为时间：',datetime.datetime.strptime('2018-11-11','%Y-%m-%d'))
#
#
# dt1=datetime.datetime.now()
# print(dt1.year)
# print(dt1.month)
# print(dt1.day)
# print(dt1.weekday())
# print(dt1.date())
# print(dt1.time())
#
#
# # ****************calendar日历模块**************
# print(calendar.calendar(2020))  #年历
#
# print(calendar.month(2019,12)) # 获取某个月份日历
#
# print('获取年份是否为闰年，为闰年则返回true:',calendar.isleap(2019))
#
# print('获取指定时间为星期几：',calendar.weekday(2018,12,17))
#
# # 求天数  1900到今天的天数
# def getsumday():
#     sum=0
#     for x in range(1900,2019):
#         if calendar.isleap(x):
#             sum+=366
#         else:
#             sum+=365
#     for x  in range(1,12):
#         if x in(1,3,5,7,8,10,12):
#             sum+=31
#         elif x in(4,6,9,11):
#             sum+=30
#         elif calendar.isleap(2019):
#             sum+=29
#         else:
#             sum+=28
#     sum+=17
#     print(sum)


#    *****************异常错误处理****************
# print(1/0)  #ZeroDivisionErro

# if True
#     print('hello world')  #SyntaxError  语法错误
#                         # IndentationError 缩进错误
# # print('2'+2)            #TypeError类型错误
#
# # print(2*2*ss)    #NameError

# 捕抓所有的异常
# try:
#     print(1/0)
#     print('hello world')
#     print('hello testcode')
# except:
#     print('代码块有异常！')

# 捕抓指定异常
# try:
#     代码块
# except 异常类型：
#     异常处理代码

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('ZeroDivisionErro')

# list1=[1,2,3,'a',4]
# for x in list1:
#     try:
#         print(x+1)
#     except:
#         print('类型不同')

# 异常类型不确定或者不清楚，可以用 Exception异常
# try:
#     file1=open('a.txt','r')
#     file1.read(10)
#     file1.close()
# except Exception as e:
#     print(e)

# 多个 异常
# try:
#     print('hello testcode')
#     file1 = open('a.txt', 'r')
#     file1.read(10)
#     file1.close()
# except ValueError as e:
#     print(e)
# except TypeError:
#     print('TypeError')
# except FileNotFoundError as err:
#     print('FileNotFoundError',err)
# except:
#     print('其他异常类型')
# else:
#     print('其他操作代码块')
# finally:
#     print('不管有没有异常都会执行的语句')


# x值大于5就抛出异常

#
# x=10
# if x>5:
#     raise ValueError('x值大于5')
# try:
#     print(1/0)
# except Exception as e:
#     print(e)

# 用traceback打印异常,可以常看到具体异常详情
import traceback

try:
    print(1/0)
except :
    traceback.print_exc()          #打印异常traceback.print_exc()
    print(traceback.format_exc()) #返回异常字符串


# 把异常写入文件
try:
    print(1/0)
except Exception as e:
    traceback.print_exc(file=open('error.txt','w+'))
#
