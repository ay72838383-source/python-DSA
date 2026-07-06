che = int(input("enter your chem marks:"))
math = int(input("enter your math marks:"))
phy = int(input("enter your phy marks :"))
total_per = (100)*(che + math+phy)/300


if (total_per>=40 and che>=33 and math>=33 and phy >= 33):
    print("you aree passed",total_per)

else:
    print("you are failed",total_per)