class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        self.c=self.a+self.b
        print("addition:",self.c)

class Child:
    def __init__(self,x,y):
        Parent.__init__(self,a,b)
        
    def multiple(self):
        self.c=self.a*self.b
        print("multiplication:",self.c)
a=int(input("enter the number:"))
b=int(input("enter the number:"))
cd=Child(a,b)
m=cd.multiple()
        
        
