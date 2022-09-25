## Python函数

#### 函数的概念

如果在开发程序时，需要某块代码多次，但是为了提高编写的效率以及代码的重用，所以把具有独立功能的代码块组织为一个小模块，这就是函数。

之前我们见过的函数:

- random.randint(1,100)：生成1到100之间的随机数
- print("hello", 2, 3.14)：打印输出内容
- “Clark 18”.split()：拆分字符串

#### 简单函数

```python
'''
第一步：定义函数
def 函数名():
    语句
第二步：调用函数
函数名()
'''
# 定义函数
def printline():
    print('-'*30)
# 调用函数
printline()
```



#### 带参数的函数

- 在调用函数时，如果需要把一些数据一起传递过去，被调用函数就需要用参数来接受
- 参数列表中变量的个数根据实际传递的数据多少来确定
- 设定参数的三种方法
  - 位置实参（有顺序，形参和实参一一对应）
  - 关键词参数（没有顺序）
  - 函数默认值参数（默认值参数需要放到函数参数的最后，调用的时候可以不填）

```python
# 定义函数
def add2num(a, b):
    c = a + b
    print(c)
# 调用函数
add2num(11, 22)

def func(a, b):
    # c = a + b
    c = a**b
    print(c)

# func(11, 22)
# 位置实参
func(2, 3)
# 关键词参数（没有顺序）
func(a=3, b=2)

# 默认值参数
def func(a, b, method='add'):
    if method == 'add':
        c = a + b
    elif method == 'exp':
        c = a**b
    # else:
    #     print("暂不支持")
    print(c)

func(1,3, method='exp')
```

**[练习：补齐以上减法，乘法和除法等相关代码用不同的参数调用方式进行处理]()**



#### 带return语句的函数

- 看一个函数到底有没有返回值，就看有没有return，因为只有return才可以返回数据
- 函数可以返回字典，列表等容器变量， 返回多个值
- 函数中，可以有多个return语句，但是只要执行到一个return语句，那么就意味着这个函数的调用完成

```python
# 单个返回值
def add2num(a, b):
    c = a + b
    return c
# 直接print函数输出
print(add2num(11, 22))
# 用变量接收函数的返回值
result = add2num(11, 22)
print(result)

# 返回一个字典变量
students = {
    'clark':{'id':'A001', 'grade':78},
    'rita':{'id':'A002', 'grade':88},
    'raye':{'id':'A003', 'grade':68},
    'aaa':[1,2,3,4]
}
def stu_info(name):
    if name in students:
        return students[name]
    else:
        return None
print(stu_info('clark'))

# 多个返回值
def div2num(a, b):
    shang = a//b
    yushu = a%b
    return shang, yushu
var1, var2 = div2num(5, 2)
print('商为%d,余数为%d'%(var1, var2))
```

[**练习**]()

1. [**写一个打印一条横线的函数（提示：横线是由30个“-”组成）**]()
2. [**写一个函数，可以通过输入的参数，打印出自定义条数的横线。（提示：调用上面的函数）**]()

```python
def printline():
    print('-'*30)
def printnumline(rows):
    i = 1
    while i <= rows:
        printline()
        i = i+1
printnumline(4)
```



#### 匿名函数

- 定义：匿名函数不需要显示地定义函数名，使用【lambda + 参数 +表达式】的方式

- 语法：lambda [arg1 [,arg2, ... argN]] : expression  （类比之前定义函数没有return语句）

- 特点：

  - 可以传入多个参数（也可以一个参数不传），但只能有一个表达式
  - 不用取名称，因为给函数取名是比较头疼的一件事，特别是函数比较多的时候
  - 语法结构简单，不用使用def 函数名(参数名)

  ```python
  # 用匿名函数实现前面的功能
  add2num = lambda x, y: x+y
  add2num(11,22)
  div2num = lambda x,y : (x//y,x%y)
  div2num(5,2)
  ```

- 特殊使用场景：(函数作为参数进行传递)

  ```PYTHON
  # 对一个嵌套列表实现指定元素的排序
  lst1 = [['clark', 76], ['rita', 55], ['raye', 43], ['michal', 57], ['tracy', 88]]
  print(sorted(lst1, reverse=True))
  print(sorted(lst1, key=lambda x: x[1], reverse=True))
  ```

  

#### 函数在模块中的使用

- 定义：实际开发中代码都会包含在不同的文件中，以.py后缀结尾的文件，叫做模块

- 引入方式：

  - import 模块名
  - import 模块名 as 别名
  - from 模块名 import 函数1, 函数2  （表示该模块下的函数1，函数2可以直接使用）
  - from 模块名 import *

- 练习：生成两个python文件，功能描述如下：

  - 文件1：定义一个学生的字典列表（如下），定义一个函数接收学生姓名并打印相关学生信息

    ```python
    students = {
        'clark':{'id':'A001', 'grade':78},
        'rita':{'id':'A002', 'grade':88},
        'raye':{'id':'A003', 'grade':68}
    }
    ```

  - 文件2：从键盘接受输入学生姓名，如果能找到展示字典类型变量，如果不能找到进行提示即可

    ```PYTHON
    import student_query
    
    while True:
        stu_name = input("请输入学生姓名：")
        if stu_name in student_query.students:
            print(student_query.get(stu_name))
        else:
            print("没有该学生！")
    ```

    

#### 变量的作用域（全局变量和局部变量）

全局变量：作用域为定义的模块，从定义位置开始到模块结束为全局变量的作用域

局部变量：在函数体中声明的变量，不同的函数可以定义相同的名字，彼此无关

```PYTHON
# 只有全局变量的时候，函数中没有定义该变量，会调用全局变量
# 全局和局部变量相同的名字，局部变量优先使用，没有局部变量默认使用全局变量
# 在函数中声明全局变量用global

def test1():
    a = 100  # 函数内部定义的变量为局部变量
    print(f'test1--修改前a={a}')
    a = 200
    print(f'test1--修改后a={a}')

def test2():
    a = 500 # 不同函数之间的局部变量可以相同，彼此无关
    print(f'test2--a={a}')

test1()
test2()
```





