# -*- coding:utf-8 -*-
# @Time :2019/12/15 20:05
# @Author   :testcode_susu
# @Email    :2804555260@qq.com
# @File :class_07_1.py

import os
# file1=open('1.txt','r+')
# file1.write('hello testcode!')
# file1.close()

# 打开文件并进行编辑
# file1=open('1.txt','a')
# # file1.write('hello feng!')  #把字符串写入文件
# file1.writelines(["\n",'hello chen\n','hello feng2\n',"hello ji"])
# file1.close()

# 文件读取
# file2=open('1.txt','r')
# print(file2.read(5)) #读取文件n个字节，如果n不设置或者设置为负数则读取全部内容
# file2.close()

#读取所有内容
# file2=open('1.txt','r')
# # print(file2.read())  #读取文件n个字节，如果n不设置或者设置为负数则读取全部内容
# print(file2.read(-3))
# file2.close()

# file2=open('1.txt','r')
# print(file2.readline()) #读取整行
# print(file2.readline())# 第几行
# print(file2.readline())
# file2.close()

# file2=open('1.txt','r')
# # print(file2.read())
# # print(file2.readlines())    #返回文件所有行列表
# # 结果展示第一行内容：
# for line in file2.readlines():
#     print(line)
# file2.close()

# 从指定某个位置进行读取内容
# file3=open('1.txt','r')
# file3.seek(6,0)
# print(file3.readline())
# file3.seek(0,1)
# print(file3.read(8))
# file3.close()

# file3=open('1.txt','r')
# file3.seek(53,0)
# print(file3.read(8))
# file3.close()

# file3=open('1.txt','r')
# file3.read()
# print('文件指针的位置:',file3.tell())
# file3.seek(0,0)
# print('文件指针调整后的位置:',file3.tell())
# print(file3.readline())
# print('文件读取第一行后指针位置:',file3.tell())
# file3.close()

# 文件属性
# file4=open('1.txt','r')
# # print('文件属性:',file4.name,file4.mode,file4.encoding,file4.closed)
# # print('文件名：',file4.name)
# # file4.close()


# # Python中使用with...as...语法打开文件。
# with open("1.txt","a+") as file1:
# 		file1.write("hello world")

# path=r'C:\Users\Administrator\Desktop\2.txt'
# with open(path,'w+') as file2:
#     file2.write("hello chen\n hello pinbo\n hello yusheng\n")

# path=r'C:\Users\Administrator\Desktop\aa'
# os.mkdir(path)  #创建文件夹
# print('已创建完成')

# path = r'C:\Users\Administrator\Desktop\bb\cc\dd'
# os.makedirs(path)# 创建多级目录
# print('已创建多级目录')


# path=r'C:\Users\Administrator\Desktop\aa'
# os.rmdir(path)  #删除空目录
import shutil

# path= r'C:\Users\Administrator\Desktop\bb\cc\dd'
# os.rmdir(path)  #删除空目录
# shutil.rmtree(path)#删除非空目录

# oldpath= r'C:\Users\Administrator\Desktop\bb\cc'
# newpath= r'C:\Users\Administrator\Desktop\bb\c1'
# os.rename(oldpath,newpath)   #d对文件或目录重命名
# E:\VIP\code\cema_python\class_07\class_07_1.py
import stat

print('获取当前路径:',os.getcwd())  #获取当前路径

# 获取文件权限
# path=r'C:\Users\Administrator\Desktop\bb'
# print(os.access(path,os.F_OK))  #访问文件是否存在
# print(os.access(path,os.W_OK))
# print(os.access(path,os.R_OK))
# print(os.access(path,os.X_OK))

# 设置文件权限chmod

# OTH (other) 其他
# GRP(group)  用户组
# USR(user) 所属用户
# X 可执行
# W  可写
# R 可读
path=r'C:\Users\Administrator\Desktop\bb'
os.chmod(path, stat.S_IRUSR) #所属用户设为可读权限
os.chmod(path,stat.S_IRWXG)  #用户组全部权限（可读可写可执行）














