p1 = "make a lot of money"
p2 = "buy now"
p3 = "subcribe now "
p4 = "click this "
mess = input("enter your mess:")
if((p1 in mess)or (p2 in mess)or (p3 in mess) or(p4 in mess)):
    print("this comment is spam")

else:
    print("this comment is not spam")