class calcultor :
    def __init__(self,n):
        self.n= n 
    def square(self):
        print(f"the square is {self.n*self.n}")

a = calcultor(4 )
a.square()