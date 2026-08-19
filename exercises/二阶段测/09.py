class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height

if __name__=='__main__':
    r1=Rectangle(3,5)
    print(r1.area())