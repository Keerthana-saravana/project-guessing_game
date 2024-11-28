class Natural():
    def num(self,i,n):
        self.i=i
        self.n=n
        while(i<n+1):
            print(i)
            i+=1
i=int(input("enter starting:"))
n=int(input("enter ending:"))
x=Natural()
x.num(i,n)
