#matrix multiplication
def matrix_multiplication():
    n=int(input("enter row:"))
    m=int(input("enter column:"))
    a=[]
    b=[]
    mul=[]
    for i in range(0,n):
        b1=[]
        for j in range(0,m):
            c=int(input("Array elements:"))
            b1.append(c)
        a.append(b1)
    print("matrix_1=",a)
    for i in range(0,n):
        d=[]
        for j in range(0,m):
            e=int(input("Array elements:"))
            d.append(e)
        b.append(d)
    print("matrix_2=",b)
    print("Matrix 1:")
    for i in range(0,n):
        for j in range(0,m):
            print(a[i][j],end=" ")
        print()
    print("Matrix 2:")
    for i in range(0,n):
        for j in range(0,m):
            print(b[i][j],end=" ")
        print()
    for i in range(0,n):
        for j in range(0,m):
            s=0
            for k in range(0,m):
                s=s+(a[i][k]*b[k][j])
            print(s,end=" ")
        print()
matrix_multiplication()
        
        