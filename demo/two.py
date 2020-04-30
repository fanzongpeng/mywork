# 1、定义一个列表[1, 2, 3]，并将列表中的头尾两个元素对调。对调后为[3, 2, 1]
list1 = [1, 2, 3]
print(len(list1))
list1[0], list1[len(list1) - 1] = list1[len(list1) - 1], list1[0]
print(list1)
#
# 2、定义一个列表，并将列表中的指定位置的两个元素对调。对调第一个和第三个元素

# 列表如下：
# 对调后结果：[19, 65, 23, 90]
list2 = [23, 65, 19, 90]
list2[0], list2[2] = list2[2], list2[0]
print(list2)
#
# 3、对列表[10, 11, 12, 13, 14, 15]
# 翻转，调整后为[15, 14, 13, 12, 11, 10]
list3 = [10, 11, 12, 13, 14, 15]
list3.reverse()
print(list3)

#
# 4、判定6是否包含列表
list4 = [1, 6, 3, 5, 3, 4]
print(list4.index(6))
print(list4.count(6))
for i in list4:
    if i == 6:
        print("True")

# 5、[1, 6, 3, 5, 3, 4]
# 转换为元组
list5 = [1, 6, 3, 5, 3, 4]
print(tuple(list5))
#
# 6、根据列表[1, 6, 3, 5, 3, 4]
# 作为新字典的key, 对应key的初始值为0，并打印新字典对象
list6 = [1, 6, 3, 5, 3, 4]
##内置函数
print(dict.fromkeys(list6, 0))
##循环


#
# 7、循环打印出字典
# {'name': 'aming', 'age': 18, 'school': 'cema'}
dict1 = {'name': 'aming', 'age': 18, 'school': 'cema'}
# 中的所有键和值，
for k, v in dict1.items():
    print(k, v)
# 9、分别有两个集合
# {1, 2, 1, 3, 4, 5, 6, 7}，{1, 2, 3, 8, 9, 7, 10}，求两个集合的差集、并集、交集（不做）
set3 = {1, 2, 1, 3, 4, 5, 6, 7}
set4 = {1, 2, 3, 8, 9, 7, 10}
#print(set3 - set4)
#print(set4 - set3)
##print(set3 | set4)
#print(set3 & set4)
#
#
# 10、判断9题中两个集合如果存在相同元素，则打印重复，否则打印无重复
print(set3.isdisjoint(set4))
if set3.isdisjoint(set4):
    print('无重复')
else:
    print("重复值为"+str(set3.intersection(set4)))




# 11、list7 = [1, 2, 3, 4, 5]
# 根据列表中的元素作为字典中的key, 及初始值为0，打印这个新的字典，不用fromkey方法实现
list7 = [1, 2, 3, 4, 5]
dict2 ={}
for i in list7:
    dict2[i] = 0
print(dict2)
#
#
