'''
字典和列表有3个地方是一样的：1.有名称；
2.要用=赋值；3.用逗号作为元素间的分隔符。

而不一样的有两处：1.列表外层用的是中括号[ ]，字典的外层是大括号{ }

'''
students=['小明','小红','小刚']
scores={'小明':95,'小红':90,'小刚':90}

'''
列表中的元素是自成一体的，而字典的元素是由一个个键值对构成的，用英文冒号连接。
如'小明':95，其中我们把'小明'叫键（key），95叫值(value)。

这样唯一的键和对应的值形成的组合，我们就叫做【键值对】，
上述字典就有3个【键值对】：'小明':95、'小红':90、'小刚':90

'''
print(len(students))
print(len(scores))
#字典的索引，和列表通过偏移量来索引不同，字典靠的是键
#字典中提取对应的值的用法。和列表相似的是要用[ ]，
#不过因为字典没有偏移量，所以在中括号中应该写键的名称，即字典名[字典的键]


'''删除字典里键值对的代码是del语句del 字典名[键]，
而新增键值对要用到赋值语句字典名[键] = 值。
'''
print(scores['小红'])
scores['小刚']=92
scores['小明']=85
print(scores)
score={
    '第一组':{'小明':95,'小红':90,'小刚':100,'小美':85},
    '第二组':{'小强':99,'小兰':89,'小伟':93,'小芳':88}
    }
print(score['第一组']['小刚'])
print(score['第一组']['小红'])
# 最外层是大括号，所以是字典嵌套列表，先找到字典的键对应的列表，再判断列表中要取出元素的偏移量
student={
    '第一组':['小明','小红','小刚','小美'],
    '第二组':['小强','小兰','小伟','小芳']
    }
# 最外层是中括号，所以是列表嵌套字典，先判断字典是列表的第几个元素，再找出要取出的值相对应的键
score1 = [
    {'小明':95,'小红':90,'小刚':100,'小美':85},
    {'小强':99,'小兰':89,'小伟':93,'小芳':88}
    ]
print(student['第一组'][3])
print(score1[1]['小强'])