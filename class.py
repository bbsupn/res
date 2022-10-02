from re import S


class Students:
    def __init__(self,name,score) -> None:#建立构造函数时self参数必须第一位
        self.name=name
        self.score=score

    def say_score(self):
        print(f'同学{self.name}的成绩是{self.score}分!')

s1=Students('clark',60)#实例化一个对象
s1.say_score()
s2=Students('rita',70)
s2.say_score()