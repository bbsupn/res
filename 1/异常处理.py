# grade = input("请输入你的成绩：")
# grade = int(grade)
# print(f"你的成绩是{grade}分")

# try - except
# try - except - finally


# grade = input("请输入你的成绩：")
# while True:
#     print('#'*30)
#     try:
#         grade = int(grade)
#     except ValueError as e:
#         # print(e)
#         print("你的输入有误，请重新输入：" + e)
#         continue
#     print(f"你的成绩是{grade}分")


# lst1 = []
# while True:
#     print('#'*20)
#     grade = input("请输入成绩：")
#     try:
#         grade = int(grade)
#     except ValueError as e:
#         print("你输入的信息有误，请重新输入，错误信息为：", e)
#         continue
#     print(grade)


# except Exception as e:

f = open('写出文件.txt', 'w')
try:
    while True:
        data = input("输入信息：")
        if data == 'quit':
            break
        data = int(data)
        f.write(str(data) + '\n')
except Exception as e:
    print("错误信息为：", e)
# 不管上面是否抛出异常都会执行
finally:
    print("aaaaaa")
    f.close()