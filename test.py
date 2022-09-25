# 模块引入方法一：
# import computemode
# computemode.add(1, 5)
# 模块引入方法二：
# import computemode as cm
# cm.sub(8, 4)
# 模块引入方法三：
# from computemode import add, sub
# add(4, 8)
# 模块引入方法四：
# from computemode import *
# print(a)

# 文件一：
# 1.students字典变量
# 2.定义一个函数实现接收学生姓名单元对应学生信息的功能
# 文件二：
# 1.导入文件一模块
# 2.实现一个不断查询学生姓名对应的学生信息的功能
#     a.可以退出，输入quit输出程序
#     b.展现查询结构信息（{'id':'A001', 'grade':78},
#         "没有该学生信息"）

import computemode
while 1:
    name=input("请输入学生姓名输入quit结束：")
    if name=='quit':
        break
    computemode.fun1(name)

