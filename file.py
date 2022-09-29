#open()
#打开文件
#f=open('file.txt')#文件句柄
#读取文件
#print(f.read())#读取文件内容
#按行读取
#for line in f:
 #   print(line.strip())#把每行数据左右两边的空白字符截取掉
#一次性把每行数据都读取出来，生成一个列表
#readline()
#print(f.readlines())
#for line in f.readlines():
 #   print(line.split('\n')[0])

#with打开文件
#with open('file.txt','r') as f:
    #print(f.read())
#关闭文件
#f.close()
dic={}
with open('./1/英文单词.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        en,cn=line.split()
        en=en.strip()
        dic[en]=cn
while True:
    word=input("请输入英文或输入quit退出:")
    if word=='quit':
        exit(0)
    else:
        if word in dic:
            print(f"翻译结果为:{dic[word]}")
        else:
            print("字典内未找到结果")

#zip()打包函数
