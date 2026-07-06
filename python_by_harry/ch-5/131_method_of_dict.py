# m= {} it is use for make empty dict
mark = {
    "prince":10,
    "aashish":11,
    "himanshu":-100

}
#print the item of dict
print(mark.items())


#print the keys of dict
print(mark.keys())

#print the value of dict 
print(mark.values())


#update method of dict
mark.update({"aashish":10,"harry":9})
print(mark)

#get the value of dict
print(mark.get("prince"))