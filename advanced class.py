class fridge:
    def __init__(self):
        self.NumberOfItems = 0
        self.DoorOpen = False
        self.isRunning = True
        
    def printFridge(self):
        print("Hello I am fridge with", self.NumberOfItems, "Number of items")
        if self.DoorOpen == False:
            print("and my door is closed")
        else:
            print("and my door is open")
            
        if self.isRunning == True:
            print("I am running... come and catch me!")
        else:
            print("I am not running... but don't let your food spoil")
    
    def openDoor(self):
        self.DoorOpen = True
    def closeDoor(self):
        self.DoorOpen = False
        
        
    def fillFridge(self,num):
        if self.DoorOpen == True:
            self.NumberOfItems += num
            print("You just added",num,"food to the fridge")
        else:
            print("You can't put stuff into the fridge when the door is shut")
    def MakeDinner(self):
        if self.DoorOpen == True:
            self.NumberOfItems -= 10
        else:
            print("You can't take stuff out when the door is closed")
            
#------------------------------------------------------------------------------------------------------------------
f1 = fridge()#constructor
f1.printFridge()
print()
food = int(input("How much food to add?"))
f1.fillFridge(food)
print()
f1.openDoor()
f1.fillFridge(food)
f1.printFridge()
print()
f1.MakeDinner
f1.closeDoor()
f1.printFridge()

            
