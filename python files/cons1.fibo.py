class Fibo:
    def __init__(self):
        self.a=int(input("enter starting:"))
        self.b=int(input("enter ending:"))
    def num(self):
        self.i=0
        self.n=1
        for x in range(self.a,self.b,1):
            self.c=self.i+self.n
            self.i=self.n
            self.n=self.c
            print("fibonacci series:",self.c)
ad=Fibo()
y=ad.num()
        
