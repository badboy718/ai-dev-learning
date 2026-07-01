class Account():
    def __init__(self,name):
        self.name = name
        self.__money = 100
    def get_money(self):
        return self.__money
    def set_money(self,money):
        self.__money = money

user=Account('金城武')
print(user.name)
#print(user.money)
print(user.get_money())
user.set_money(200)
print(user.get_money())