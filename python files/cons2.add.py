class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def num(self):
        self.c=self.a+self.b
        print("addition=",self.c)

a=int(input("enter the number:"))
b=int(input("enter the number:"))
ad=Addition(a,b)
x=ad.num()
