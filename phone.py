class Phone:
    def __init__(self,model,price,name):
        self.model=model
        self.price=price
        self.name=name
    def describe(self):
        return(f'这是{self.model}手机,平均价格{self.price}元')
    def call_friend(self):
        return(f'我在用{self.model}手机，给朋友{self.name}打电话')
s1=Phone('HuaWei',4000,'rita')
s2=Phone('IPhone',6000,'clark')
print(s1.describe())
print(s2.describe())
print(s1.call_friend())
print(s2.call_friend())
#静态方法
#@staticmethod

#@classmethod

#@property

