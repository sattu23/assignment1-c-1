#Challenge 1: Square numbers and return their sum>>>>>

class point:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def add(self,a,b,c):
        a=self.x**2
        b=self.y**2
        c=self.z**2
        return a,b,c
    def sqsum(self):
        square=self.x**2 +self.y**2 +self.z**2
        return square
num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
num3=int(input('enter num3:'))
obj=point(num1,num2,num3)
print(obj.sqsum())


