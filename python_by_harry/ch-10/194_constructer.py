class employe : 
    name = "prince"
    lang = "py"
    salary = 50 
    def __init__(self, name, salary, lang):
       self.name=name
       self.salary=salary
       self.lang=salary
       print("this is good")
       
    def getinfo(self):
        print(f"the lang is {self.lang}.the salary is{self.salary}")
@staticmethod
def greet():
  print("good")
harry = employe("harry", 135555)
print(harry.name,harry.salary, harry.lang)
greet()
harry.lang="js"
harry.getinfo()
