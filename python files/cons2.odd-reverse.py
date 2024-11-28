class Odd_reverse:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def num(self):
        while (self.b>=self.a):
            if(self.b%2==1):
                print("odd reverse:",self.b)
            self.b-=1
a=int(input("enter the starting:"))
b=int(input("enter the ending:"))
ad=Odd_reverse(a,b)
x=ad.num()

        
