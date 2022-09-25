class Students: # 类名的首字母要大写，多个单词满足驼峰原理
    def __init__(self, name, score): # 建立构造函数时self参数必须位于第一个位置
        self.name = name
        self.score = score
    def say_score(self):
        print(f"同学{self.name}的成绩是{self.score}分！")
s1 = Students('clark', 60) # 实例化一个对象
s2 = Students('rita', 70)
s1.say_score()
s2.say_score()

# 守， 破， 离  堆量
# **[练习：建立一个Phone手机类]()**
#
# 1. 构造函数
#    - 有两个形参model型号和price价格
#    - 将model和price设置为self变量
# 2. 提供一个describe方法，用来描述手机信息
#    - 返回“这是{model}手机，平均价格为{price}元”
# 3. 生成一个对象并调用该类的describe方法来打印文字

class Phone:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def describe(self):
        print(f"手机型号为{self.model}，价格为{self.price}")

    # @staticmethod
    #
    # @classmethod
    #
    # @property


Phone = Phone("小米", 2399)
Phone.describe()

