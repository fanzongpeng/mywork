## 1、用print函数打印多个值
import math
import random
from os.path import join

print("hello", "aaaa" \
               "bbbb" \
               "ccc")
print("bbb")

##2、用print函数不换行打印
a = "c++"
print("python", "java", end=' ')
print(a)

##3、导入模块的方式有哪些
print('''
        1 import 模块名
        2 from 模块名 import 函数1，函数2
        3 from 模块名 import *
             ''')

##4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
print('''
    6种类型：number数字型 
    string   字符串型
    list  数组型
    set 集合
    tuple元组
    Dictionary字典
    不可变： number string tuple
    可变：list、dictionary、set
    ''')

##5、python3中可以支持哪些数值类型？'
print("python3中可以支持的树枝类型有{},{},{}".format('int', 'float', 'bool', 'complex'))

##6、判断变量类型有哪些方式，分别可以用哪些函数？
print("判断变量类型常用的函数有：%s ,% s" % ('type()', "isinstance('变量', '数据类型')"))

##7、分别对49.698作如下打印
f = 49.698
##1）四舍五入，保留两位小数
print(round(f, 2))

# 2）向上入取整
print(math.ceil(f))
# 3）向下舍取整
print(math.floor(f))
# 4）计算8除以5返回整型
print(8 // 5)
# 5）求4的2次幂
print(4 ** 2)
# 6）返回一个（1, 100）随机整数
print(random.randint(1, 100))

# 8、依次对变量a, b, c赋值为1, 2, 3
a, b, c = 1, 2, 3
print(a, b, c)
# 9、截取某字符串中从2索引位置到最后的字符子串
str1 = 'qwdnqdnkqd'
print(str1[2:])
# 10、对字符串“testcode”做如下处理：
str = 'testcode'
# 1）翻转字符串
print(str[::-1])
# 2）首字母大写
print(str.capitalize())

# 3）查找是否包含code子串，并返回索引值
print(str.find("code"))
print(str.index("code"))


# 4）判断字符串的长度
print(len(str))
# ##5）从头部截取4个长度字符串
print(str[0:4])
# ##6）把code替换为123
print(str[0:4] + '1234')
# ##7）把“testcode”字符串中的两个单词转换为列表中的元素，并打印处理

l1=[str[0:4],str[4:]]
l2=list(str)
l3=str.split()
print(l1)
print(l2)
print(l3)

# ##8）把['test', 'code'] 把list变量中的元素连接起来
s=''
l=['test', 'code']
print(s.join(l))


##11、如何打印出字符串“test\ncode”
print(r'test\ncode')
print("test\\ncode")

##12、如何创建一个空元组
c = tuple()

##13、创建一个只包含元素1的元组，并打印出该变量的类型
d = tuple('java', )
print(type(d))

##14、元组中元素可以修改？如何更新元组中的元素？
print('''元祖中元素不可修改"
        可以和其他元组连接
''' )

##15、对元组（1, 2, 3, 4, 5)做如下操作：

t=(1, 2, 3, 4, 5)
##1）取倒数第二个元素
print(t[1])


##2）截取前三个元组元素
print(t[0:3])

##3）依次打印出元组中所有元素
for i in t:
    print(i)

##16、把元组(1, 2, 3, 4, 5, 6)元素格式化成字符串
t1=(1, 2, 3, 4, 5, 6)
s0='%d%d%d%d%d%d' %t1
ss='{}'.format(t1)
print(s0,type(s0))



