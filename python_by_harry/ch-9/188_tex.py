f = open("text.txt")
c = f.read()
if("aashish" in c):
    print("yes")
else:
    print("no")
f.close