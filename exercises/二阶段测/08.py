class Person:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print(f'Hello,{self.name}!')
if __name__ == '__main__':
    p1=Person('Boxuegu')
    p1.say_hello()