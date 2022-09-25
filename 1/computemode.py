# a = 15
# b = 20
#
# def addnum(a, b, method='add'): # 形参
#     if method == 'add':
#         # b = str(b)
#         c = a+b
#         print(c)
#     elif method == 'sub':
#         c = a-b
#         print(c)
#     elif method == 'mul':
#         c = a*b
#         print(c)
#     elif method == 'div':
#         c = a/b
#         print(c)
#
# # 经过二次封装后的函数
# def add(x, y):
#     addnum(x, y)
# def sub(x, y):
#     addnum(x, y, method='sub')
# def mul(x, y):
#     addnum(x, y, method='mul')
# def div(x, y):
#     addnum(x, y, method='div')


# 文件1
# 属性
# 方法

students = {
    'clark':{'id':'A001', 'grade':78},
    'rita':{'id':'A002', 'grade':88},
    'raye':{'id':'A003', 'grade':68}
}
# name = input("请输入一个姓名：")

def fun1(name):
    for i in students:
        if name==i:
            print(students[i])
            break
    else:
        print("没有该学生")
# fun1(name)
