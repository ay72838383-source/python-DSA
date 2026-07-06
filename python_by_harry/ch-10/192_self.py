class employe : 
    name = "prince"
    lang = "py"
    salary = 50 
    def getinfo(self):
        print(f"the lang is {self.lang}.the salary is{self.salary}")

harry = employe()
harry.lang="js"
harry.getinfo()
