def matrix_add():
    n=int(input("enter row:"))
    m=int(input("enter column:"))
    a=[]
    x=[]
    sum=[]
    for i in range(0,n):
        b=[]
        for j in range(0,m):
            c=int(input("Array Element for matrix_1="))
            b.append(c)
        a.append(b)
    print(a)
    for i in range(0,n):
        d=[]
        for j in range(0,m):
            e=int(input("Array elements for matrix_2:"))
            d.append(e)
        x.append(d)
    print(x)    

    for i in range(0,n):
        for j in range(0,m):
            print(a[i][j],end=" ")
        print()
    print("matrix_1:")
    for i in range(0,n):
        for j in range(0,m):
            print(x[i][j],end=" ")
        print()
    print("matrix_2:")
    for i in range(0,n):
        for j in range(0,m):
            print("Addition:",a[i][j]+x[i][j])
            sum.append(a[i][j]+x[i][j])
        print(sum)
    for i in range(0,n):
        for j in range(0,m):
            print(a[i][j]+x[i][j],end=" ")
        print()
matrix_add()
