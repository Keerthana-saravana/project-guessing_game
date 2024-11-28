class Natural:
    def num(self,i,n):
        a=0
        self.i=i
        self.n=n
        while(self.i<=self.n):
            a=self.i+a
            self.i+=1
        return a
i=int(input("enter starting:"))
n=int(input("enter ending:"))
ad=Natural()
x=ad.num(i,n)
print("sum of natural numbers:",x)

            
