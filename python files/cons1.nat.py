class Natural:
    def __init__(self):
        self.a=int(input("enter starting:"))
        self.b=int(input("enter ending:"))
    def num(self):
        while(self.a<=self.b):
            print("natural numbers:",self.a)
            self.a+=1
ad=Natural()
x=ad.num()
