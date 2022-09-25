students={
    'clark':{'id':'A001','grade':78},
    'rita':{'id':'A002','grade':88},
    'raye':{'id':'A003','grade':68}
}
def func(name):
    for i in students:
        if name==i:
            print(students[i])
            break
        else:
            print("请重试，没有找到该学生")
