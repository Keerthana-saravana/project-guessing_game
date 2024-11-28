class Perfect:
    def num(self,i):
        self.i=i
        n=1
        c=0
        while(n<self.i):
            b=self.i%n
            if b==0:
                c=n+c
            n+=1
        if c==self.i:
            print("pefect number")
        else:
            print("not perfect number")
i=int(input("enter the number:"))
ad=Perfect()
x=ad.num(i)
            
