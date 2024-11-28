class Prime:
    def num(self,a):
        self.a=a
        n=1
        c=0
        while(n<=self.a):
            b=self.a%n
            if b==0:
                c=c+1
            n+=1
        if c==2:
            print("it is prime")
        else:
            print("it is not prime")
a=int(input("enter the number:"))
ad=Prime()
x=ad.num(a)
