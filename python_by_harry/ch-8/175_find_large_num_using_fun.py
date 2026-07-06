def l (a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c 



a = int(input("enter your no:"))
b = int(input("enter your no:"))
c = int(input("enter your no:"))
print("this is larger than other no:",l(a,b,c))
