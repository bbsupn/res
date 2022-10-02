f = open('logger.log', 'a')
try:
    while True:
        data = input("输入信息：")
        if data=='exit'|'quit':
            break
        data = int(data)
        f.write(str(data) + '\n')
except Exception as e:
    print("错误信息为：", e)
# 不管上面是否抛出异常都会执行
finally:
    print('程序已结束')
    f.close()