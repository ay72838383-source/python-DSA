a = int(input("enter your 1st no:"))
a1 = int(input("enter your 2nd no:"))
a2 = int(input("enter your 3rd no:"))
a3 = int(input("enter your 4th no:"))

if(a>a1 and a>a2 and a>a3):
    print("a is larger",a)

elif(a1>a2 and a1>a3):
    print("a1 is larger",a1)


elif(a2>a3):
    print("a2 is larger", a2)

else:
    print("a3 is larger",a3)
