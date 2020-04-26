list1=["郭易","汤碗珍",'Y','余生']
hello='''
-----------------------欢迎进入T666班学生管理系统-----------------------------\n
请选择系统功能：\n
0:显示所有学员信息\n
1:添加一个学员信息\n
2:删除一个学员信息\n
3:修改一个学员信息\n
4:查询一个学员信息\n
exit:退出学生管理系统\n
请输入你的操作：
'''

def addinfo():
    newname=input('请输入增加人的姓名：')
    list1.append(newname)
    print(list1)

def caozuo():
    num=input(hello)
    if num=='0':
        print(list1)
        caozuo()
    elif num=='1':
        addinfo()
        caozuo()


caozuo()



