class Prime:
    def __init__(self):
        self.a=int(input("enter a number:"))
    def num(self):
        n=1
        b=0
        while(n<=self.a):
            self.i=self.a%n
            if self.i==0:
                b=b+1
            n+=1
        if b==2:
            print("it is prime")
        else:
            print("it is not prime")
ad=Prime()
x=ad.num()
