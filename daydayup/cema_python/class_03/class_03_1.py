# -*- coding:utf-8 -*-
# @Time :2019/12/5 20:44
# @Author   :testcode_susu
# @Email    :2804555260@qq.com
# @File :class_03_1.py

#创建list
list1=[1,2,3,4,'susu','xuzhu']
print(type(list1[4]),list1[-2])
print('截取最后两个元素：',list1[-2:])
print('list翻转:',list1[::-1])
list1[-1]='xiaolongnv'
# print('修改最后一个元素：',list1)
# del list1[0]
# print('删除第一个元素的新list',list1)
# list1.clear()  #清空所有元素
# del list1    #删除list对象
# print(list1)

# List支持运算操作（+、*、 in、not in）
list2=[5,6,7,8]
print(list1+list2)
print(list2*2)
if 5   in list2:
    print('存在')
else:
    print('不存在')

list3=[list1,list2,1,2,'susu']
print(list3)

# 追加元素
list4=[1,2,3,4,5,6]
list5=[7,8,9,10]
list4.append(7)
print('追加元素：',list3)
list4.insert(0,0)
print('指定位置增加元素:',0)
# 批量增加多个元素
list4.extend(list5)
print(list4)

print(list5)
list5.pop()
print(list5)
list5.pop(0)
print(list5)
list5.remove(9)
print(list5)

list6=[1,2,3,4,5,6,1]
if list6.count(1)>0:
    print('1的索引值：',list6.index(1,0,len(list6)))
else:
    print('no find')
list6.reverse()
print('反转：',list6)
list6.sort() #默认按升序
print('排序后的list',list6)
list6.sort(reverse=True)
print('降序后的list',list6)

tup3=(1,2,3,4)
print(list(tup3))

# 创建字典
dict1={'name':'dfbbzyl','age':18}
print(dict1)
print(dict1['name'],dict1['age'])
dict1['age']=20
print(dict1)
dict1['school']='cema'
print(dict1)


# list7=[1,2,3,4,5]根据列表中的元素作为字典中的key,及初始值为0，打印这个新的字典
list7=[1,2,3,4,5]
dict2=dict.fromkeys(list7,0)
print(dict2)

print(dict1.items())
for x,j in dict1.items():
    print('key:',x)
    print('value',j)
print(dict1)

for x in dict1.keys():
    print(x)
for x in dict1.values():
    print(x)

print(dict1.get('name','notfind'))
dict2={'name02':'pinbo'}
dict1.update(dict2)
print(dict1)
dict1.pop('school')
print(dict1)
dict1.popitem()
print(dict1)

dict3=dict1.copy()
print(type(dict3),dict3)

# 集合set
set1={'baidu','taobao','jingdong','alibaba','taobao',1,2}
print(set1)
set2=set()
print(type(set2))

set1={1,2,3,4,5}
set2={6,7,8,9,10,1,2,3}
# print('set1&set2交集：',set1&set2)
print('set1|set2并集：',set1|set2)
print('set1-set2差集',set1-set2,set2-set1)
print('set1^set2异或',set1^set2)
#
# if  1 in set1:
#     print('存在')
# else:
#     print('不存在')

# set1={1,2,3,4,5}
# set1.add(6)
# print(set1)
#
# set2={1,6,7,8,9,10,1,2,3}
# set1.update(set2)
# print('把set2更新到set1：',set1)
#
# set1={1,2,3,4,5}
# # print('删除元素为：',set1.pop())
# # print('删除元素后set1为：',set1)
# set1.remove(5)
# print(set1)
# # set1.remove(8)
# set1.discard(8)
# print(set1)
# if 8 in set1:
#     set1.remove(8)
# else:
#     print('not find')


set1={1,2,3,4,5}
set2={6,7,8,9,10,1,2,3}
print('交集',set1.intersection(set2))
print('并集:',set1.union(set2))
print('set1-set2差集',set1.difference(set2))
print('set1^set2',set1.symmetric_difference(set2))

# issubset()指定集合是否参数集合的子集，是子集返回True，否则返回 False。
set1={1,2,3,4,5}
set2={6,7,8,9,10,1,2,3}
set3={6,7,8}
if set1.issubset(set2):
    print('set1是set2的子集：则打印True')
else:
    print('False')
if set3.issubset(set2):
    print('True')
else:
    print('False')

if set1.isdisjoint(set3):
    print('set1和set2没有相同元素：True')
else:
    print('False')

set1.isdisjoint()
print()



















