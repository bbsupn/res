#第一步：定义函数


#def printfunc():
 #   print('#'*30)
#第二步：调用函数
#printfunc()

#带参数函数（实参、形参)
'''
def addnum(a,b):#实参
    c=a+b
    print(c)
'''

'''def addnum(a,b):#形参
    b=str(b)
    c=a+b
    print(c)
'''
'''
def addnum(a,b,method='add'):
    if method=='add':
       # b=str(b)
        c=a+b
        print(c)
    elif method=='sub':
        c=a-b
        print(c)
'''
'''
def addnum(a,b,method='add'):
    if method=='add':
       # b=str(b)
        c=a+b
        print(c)
    elif method=='sub':
        c=a-b
        print(c)
    elif method=='mul':
        c=a*b
        print(c)
    elif method=='div':
        c=a/b
        print(c)
'''
#1.位置传参(实参和形参的位置要一一对应)
#addnum('clark',11)#实参
#2.关键字传参
#addnum(b=11,a='clark')
#3.默认值传参
'''
def add(x,y):
    addnum(x,y)
def sub(x,y):
    addnum(x,y,method='sub')

add(3,5)
sub(3,5)

'''
#addnum(11,22,method='sub')
#sub()
#add(a,b)

###############################


#函数的返回值


'''
def addnum(a,b,method='add'):
    if method=='add':
       # b=str(b)
        c=a+b
        return c
result=addnum(1,2)
print(result)
'''
'''
students={
    'clark':{'id':'A001','grade':78},
    'rita':{'id':'A002','grade':88},
    'raye':{'id':'A003','grade':68},
    'aaa':[1,2,3,4]
}

def stu_info(name):
    if name in students:
        return students[name]
    else:
        return None
print(stu_info('clark'))
'''
#return可以返回多个值
#5/2 商和余数都要返回
'''
def funname(a,b):
    shang=a//b
    yushu=a%b
    return shang,yushu

var1,var2=funname(5,2)
print(var1)
print(var2)
'''
'''
def compute(a,b,method='add'):
    if method=='add':
       # b=str(b)
        c=a+b
        return c
    elif method=='sub':
        c=a-b
        return c
    elif method=='mul':
        c=a*b
        return c
    elif method=='div':
        c=a/b
        return c
print(compute(2,5,method='mul'))
'''
#看一个函数到底有没有返回值，就看有没有return，因为只有return才可以返回数据
#函数可以返回字典,列表等容器变量,返回多个值
#函数中，可以有多个return语句，但是只要执行到一个return语句，那么就意味着这个函数的调用完成
'''
def printline():
    print('-'*30)
printline()
def prilines(num):
    i=0
    while i<num:
        printline()
        i+=1
n=int(input("n:"))
prilines(n)
'''
######################
#匿名函数
'''
add2num=lambda x,y:x+y
print(add2num(11,22))
div2num=lambda x,y:(x//y,x%y)
print(div2num(5,2))
'''

#lst1=[['clark',76],['rita',55],['raye',43],['michal',57],['tracy',88]]

#print(sorted(lst1))
#lst1.sort(key=)
#key是对多维列表的某个子元素进行排序处理

#print(sorted(lst1,key=lambda x:x[1],reverse=True))#按2号元素降序排列

###########################

#作用域(局部变量、全局变量)

'''
a=300
def test1():
    #global a
    a=300
    a=a+1
    print(f'test1,a={a}')

def test2():
    print(f'test2,a={a}')

test1()
test2()
'''


