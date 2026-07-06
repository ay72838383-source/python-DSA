'''from random import randint
class train :
    def __init__(self, trainno):
        self.trainno = trainno

    def book(self,trainno,fro,to):
        print(f"ticket is booked train no:{self.trainno}from{fro}to {to}")
   
    def getstatus(self):
         print(f"train no :{self.trainno} is  running on time ")

    def getfare(self,fro,to):
        print(f"ticket fare train no:{self.trainnom}from{fro}to {to} is {randint(222,555)}")

t = train(550)
t.book("Rampur","Delhi")
t.getstatus()
t.getfare("Rampur", "Delhi")'''

from random import randint

class Train:
    def __init__(self, trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print(f"Ticket is booked. Train no: {self.trainno} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainno} is running on time.")

    def getfare(self, fro, to):
        print(f"Ticket fare for train no: {self.trainno} from {fro} to {to} is {randint(222,555)}")

t = Train(550)

t.book("Rampur", "Delhi")
t.getstatus()
t.getfare("Rampur", "Delhi")