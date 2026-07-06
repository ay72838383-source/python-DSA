class calcultor :
    def __init__(self,n):
        self.n= n 
    def square(self):
        print(f"the square is {self.n*self.n}")
    @staticmethod
    def gg():
        print("gtyf")

a = calcultor(4 )
a.gg()
a.square()
