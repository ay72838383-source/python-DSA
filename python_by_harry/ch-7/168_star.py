


n = int(input("enter your num "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n, end=" ")

    else:
        print("*",end="")
        print("*"*(2-n),end=" ")
        print("*",end="")
    print("")