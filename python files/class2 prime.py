class Prime():
    def num(self,i):
        self.i=i
        self.b=0
        self.n=1
        while self.n<=self.i:
            self.a=self.i%self.n
            if self.a==0:
                self.b=self.b+1
            self.n+=1
        if self.b==2:
            print("it is prime")
        else:
            print("it is not prime")
i=int(input("enter the number:"))
x=Prime()
x.num(i)
