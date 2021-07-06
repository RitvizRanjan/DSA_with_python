def a():
    rows=int(input("enter no of rows"))
    for i in range(1,rows+1):
         for j in range(1,i+1):
            print(j,end=" ")
        for j in range(1,i+1):
            spaces=(rows*2-1)-(2*1)
            print(spaces * 2 *'',end="_")
        if i==rows:
            for y in reversed(range(1,rows)):
                    print(y, end=" ")
        else:
            for y in reversed(range(1,i+1)):
                print(y,end=" ")
        print()
a()