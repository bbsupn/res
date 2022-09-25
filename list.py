list=['小明',18,1.70]
print(list)
students=['小明','小红','小刚']
print(students[0])
#左右空，取到头；左要取，右不取
#以下，5为0起始位，9为4终止位
list1=[5,6,7,8,9]
print(list1[:])
print(list1[2:])
print(list1[:2])
print(list1[1:3])
print(list1[2:4])


list2=[1,2]
list2.append(3)
print(list2)
#append函数并不生成一个新列表，
#而是让列表末尾新增一个元素。而且，
#列表长度可变，理论容量无限，所以支持任意的嵌套。
students.append('小美')
print(students)
del students[1]
print(students)
