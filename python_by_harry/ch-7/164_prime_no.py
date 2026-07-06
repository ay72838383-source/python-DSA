n = int(input("enter your no:"))


for i in range(2,n):
    if(n%i==0):
        print("this is not prime no")
        break
else:
    print("this is prime no")