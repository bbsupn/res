# 第一步：定义函数
# def 函数名():
#     函数体
# def printfunc():
#     print('#'*30)
# # 第二步：调用函数
# printfunc()

# 带参数的函数（实参，形参）
# def addnum(a, b): # 形参
#     c = a+b
#     print(c)
# def addnum(a, b): # 形参
#     b = str(b)
#     c = a+b
#     print(c)

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

# 1. 位置传参： 实参和形参的位置要一一对应
# addnum('clark',11) # 实参
# 2. 关键字传参
# addnum(b=11, a='clark')
# 3. 默认值传参

# 经过二次封装后的函数
# def add(x, y):
#     addnum(x, y)
# def sub(x, y):
#     addnum(x, y, method='sub')
#
# sub(3, 5)

# add(a, b)
# sub()

###########################################

# 函数的返回值
# def compute(a, b, method='add'): # 形参
#     if method == 'add':
#         # b = str(b)
#         c = a+b
#         return c
#     elif method == 'sub':
#         c = a-b
#         return c
#     elif method == 'mul':
#         c = a*b
#         return c
#     elif method == 'div':
#         c = a/b
#         return c
# print(compute(2, 5, method='mul'))
# print(addnum(1, 2))
# result = addnum(1, 2)
# print(result)

# students = {
#     'clark':{'id':'A001', 'grade':78},
#     'rita':{'id':'A002', 'grade':88},
#     'raye':{'id':'A003', 'grade':68},
#     'aaa':[1,2,3,4]
# }
#
# def stu_info(name):
#     if name in students:
#         return students[name]
#     else:
#         return None
# print(stu_info('ccc'))

# return 可以返回多个值
# 5/2 商和余数都要返回
# def funcname(a, b):
#     shang = a//b
#     yushu = a%b
#     return shang, yushu
#
# var1, var2 = funcname(5,2)
# print(var1)
# print(var2)

#### 带return语句的函数

# - 看一个函数到底有没有返回值，就看有没有return，因为只有return才可以返回数据
# - 函数可以返回字典，列表等容器变量， 返回多个值
# - 函数中，可以有多个return语句，但是只要执行到一个return语句，那么就意味着这个函数的调用完成

# 课堂练习：
# def printline():
#     print('-'*30)
# def prilines(num):
#     i = 0
#     while i < num:
#         printline()
#         i += 1
# n = int(input("n:"))
# prilines(n)

# print('clark'); print('rita')

#########################################
# 匿名函数

# 在python一切皆对象
# add2num = lambda x, y: x+y
# print(add2num(11,22))
# # print(a)
# div2num = lambda x,y : (x//y, x%y)
# print(div2num(5,2))
#
# lst1 = [['clark', 76], ['rita', 55], ['raye', 43], ['michal', 57], ['tracy', 88]]
# print(sorted(lst1))
# # lst1.sort(key=)
# # key是对多维列表的某个子元素进行排序处理
# print(sorted(lst1, key=lambda x: x[1], reverse=True))

###########################################

# import 库包的名字

# - import 模块名
# - import 模块名 as 别名
# - from 模块名 import 函数1, 函数2  （表示该模块下的函数1，函数2可以直接使用）
# - from 模块名 import *

######################################################
# 作用域（局部变量，全局变量）
# def test1():
#     a = 100  # 函数内部定义的变量为局部变量
#     print(f'test1--修改前a={a}')
#     a = 200
#     print(f'test1--修改后a={a}')
# def test2():
#     a = 500 # 不同函数之间的局部变量可以相同，彼此无关
#     print(f'test2--a={a}')
# test1()
# test2()

# a = 300 #作用域为定义的模块，从定义位置开始到模块结束为全局变量的作用域
# def test1():
#     print(f'test1a={a}')
# def test2():
#     a= 500  # 局部变量
#     print(f'test2--a={a}')
# test1()
# test2()

# 在函数中声明全局变量用global
# a = 300
# def test1():
#     # global a
#     a = 300
#     a = a + 1
#     print(f'test1a={a}')
# def test2():
#     print(f'test2--a={a}')
# test1()
# test2()