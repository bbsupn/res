import lst
while 1:
    name=input('请输入查询学生姓名或输入quit退出')
    if name=='quit':
        break
    lst.func(name)