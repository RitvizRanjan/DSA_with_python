# def simpleint():
#     amount=int(input())
#     rate=int(input())
#     time=int(input())
#     si=((amount*rate*time)/100)
#     print(si)
#
# simpleint()


# def gcd():
#     a=int(input())
#     b=int(input())
#     if a<b:
#         small=a
#     else:
#         small=b
#     for i in range(1,small+1):
#         if(a%i==0 )and (b%i==0):
#             gcd=i
#             print(i)
#
# gcd()

# def aw():
#     n=int(input())
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print()

#
# def x():
#     n=int(input("enter"))
#     rev=0
#     while n>0:
#         rem=n%10
#         rev=rev*10+rem
#         n=n//10
#     print(rev)
#
# x()

# def y():
#     n=int(input("ensdsd"))
#     l=0
#     while n>0:
#         n//=10
#         l=l+1
#     print(l)
# y()



# def pattern():
#     n=int(input("no of rows:\n"))
#     for i in range(1, n+1):
#         space = n-i
#         print(space * '_', end="")
#
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
# pattern()

# def xx():
#     rows=int(input())
#     for i in range(1,rows+1):
#         spaces=rows-i
#         print(spaces * '  ', end="")
#
#         for j in range(1, i+1):
#             print(j, end=" ")
#
#         start=i-1
#         end=1
#         while start>=end:
#             print(start, end=" ")
#             start-=1
#         print()
#
# xx()


# def x():
#     r=int(input("enter the raidus"))
#     print(3.14*r*r)
# x()

# def y():
#     x=input("enter the string")
#     count=x.count('a')
#     print(count)
# y()
# def z():
#     n1=int(input())
#     n2=int(input())
#     sum=n1+n2
#
#     if 15<sum<20:
#         print("20")
#     else:
#      print(sum)
#
# z()
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