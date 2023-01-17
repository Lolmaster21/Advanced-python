import random
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isCheckedOut = False
        self.DeweyDecimalNumber = random.randrange(10, 300)
        
    def printbook(self):
        print("The book you checked out was: ", self.title)
        #if self.isChckedOut
        print("The person who took all the credit was: ",self.author)
        print("Random numbers are: ",self.DeweyDecimalNumber)
        
    def checkedOut(self):
        if self.isCheckedOut == True:
            print("this text is already checked out.")
        else:
            print("you checked out", self.title)
            self.isCheckedOut = True
        
    def checkedIn(self):
        self.isCheckedOut = False
        
    
#------------------------------------------------------------------Call function---------------------------------------------------------------------------------------
b1 = book("Gone with the window", "Axel")
b2 = book("Some random name", "Lol")
b3 = book("Random name pt.2", "idek")
b4 = book("The sequal to the random name", "Random")
#add more here

b1.printbook()
b1.checkedOut()

print("")

b2.printbook()
b2.checkedOut()

print("")

b3.printbook()
b3.checkedOut()

print("")

b4.printbook()
b4.checkedOut()


#game loop goes here
