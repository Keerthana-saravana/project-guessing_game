class Greatest:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def num(self):
        if self.a>self.b and self.a>self.c:
            print("a is greatest")
        elif self.b>self.c and self.b>self.a:
            print("b is greatest")
        elif self.c>self.b and self.c>self.a:
            print("c is greatest")
        else:
            print("all are equal")
a=int(input("enter number_1:"))
b=int(input("enter number_2:"))
c=int(input("enter number_3:"))
ad=Greatest(a,b,c)
x=ad.num()
