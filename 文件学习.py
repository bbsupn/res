# open()
# D:\python-base\0724\文件学习.py
# 打开文件
# f = open('students.txt', 'r') # f叫做文件句柄
# 读取整个文件信息
# 1. read函数读取整个文件信息
# print(f.read()) # 读取整个文件信息
# 2. 按行读取  \n
# for line in f:
#     print(line.strip()) # 把每行数据左右两边的空白字符截取掉
# 3. readlines函数一次性把每行数据都读取出来，生成一个列表
# print(f.readlines())
# for line in f.readlines():
#     print(line.split('\n')[0])  # join
# 关闭文件
# f.close()
# with语法打开文件
# with open('students.txt', 'r') as f:
#     print(f.read())
# 任务：
# 1.按行读取“英文单词.txt”文件
# 2.用英文单词作为key，翻译的汉字为value值生成一个字典类型变量
# 3.实现一个字典查询功能：
#     a.接收键盘输入的单词
#     b.进行查询，如果查到就显示单词对应的汉字，如果没有查到显示提示信息


# dic = {}
# with open("英文单词.txt", 'r', encoding='utf-8') as fp:
#     for line in fp.readlines():
#         en, cn = line.split()
#         # print(cn, ':', en, sep='')
#         en = en.strip()
#         dic[en] = cn
# # print(dic)
# while True:
#     print("#" * 30)
#     word = input("输入一个英文：")
#     if word == 'quit':
#         print("退出！")
#         break
#     else:
#         if word in dic: # 成员运算符
#             print(f"对应的中文是：{dic[word]}")
#         else:
#             print("未找到对应的英文单词！")

# lst1 = list('abcd')
# lst2 = list(range(4))
# print(lst1)
# print(lst2)
# print(dict(zip(lst1, lst2)))
# [('a',0),('b',1),()]
# zip() # 打包函数


# a = []
# lst = []
# with open('students.txt','r') as f:
#     zd = list(f.readline().strip().split(','))
#     for i in f.readlines():
#         a.append(i.split()[0].split(','))
#     for i in range(len(zd)):
#         lst.append(dict(zip(zd,a[i])))
#     print(lst)


# with open("students.txt","r") as f:
#     lines = f.readlines()
# l = []
# d = ["name","age","score"]
# for i in range(len(lines)-1):
#     info= ((lines[i+1]).strip().split(","))
#     l.append(dict(zip(d,info)))
# print(l)

# results = []
# with open("students.txt","r") as f:
#     keyslst = []
#     valslst = []
#     for ind, rowstr in enumerate(f):
#         # print(ind, ":", rowstr.strip())
#         if ind == 0:
#             keyslst = rowstr.strip().split(',')
#         else:
#             tmpdict = {}
#             valslst = rowstr.strip().split(',')
#             tmpdict = dict(zip(keyslst, valslst))
#             results.append(tmpdict)
# print(results)


#############################################
# 写入文件
# with open('text.txt','w') as f:
#     for i in range(4):
#         f.write("this is the first row!" + '\n')
#

# 练习：改进婚礼礼金程序
# with open('./婚礼礼金.txt', 'w', encoding='utf8') as f:
#     while True:
#         cusinfo = input("请输入来宾和礼金中间用空格分割：")
#         if cusinfo == 'quit':
#             break
#         print("#"*20)
#         f.write(cusinfo + '\n')
#
# moneys = []
# with open('./婚礼礼金.txt', encoding='utf8') as f:
#     for line in f:
#         name, money = line.strip().split()
#         moneys.append(int(money))
#
# print("总计：", sum(moneys))
# print("最大金额：", max(moneys))


# 绝对路径：D:\python-base\0724\students.txt
#     a. \\
#     b. r'绝对路径'
#     c. /
# \n, \t
# raw-string 原字符串
# with open('D:/python-base/0724/students.txt') as f:
#     print(f.read())

# 相对路径: 是以当前路径开始去进行查找文件的路径
# with open('./aaa/students.txt') as f:
#     print(f.read())













