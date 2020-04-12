class Car:
    def __init__(self,make,year,speed,cost,color):
        self.year = year
        self.make = make
        self.speed = 0
        self.cost = cost
        self.color = color

    def printDetails(self):
       print("NAME: " + str(self.make))    
       print("YEAR: " + str(self.year))    
       print("TOPSPEED: " + str(self.speed))    
       print("COLOR: " + str(self.color))
       print("COST: " + str(self.cost)) 
       

    def findValue(self):
        value = self.cost - 1000*(2020-self.year)
        if(value < 0):
         return 0

        else:
         return value

def createSale():
        n = str(input("\n\n\nNAME: "))
        y = int(input("YEAR: "))
        s = int(input("TOP-SPEED: "))
        c = int(input("COST: "))
        col = str(input("COLOR: "))
        return Car(n,y,s,c,col)



vehicle = createSale()
vehicle.printDetails()
print("Actual Value: " + str(vehicle.findValue()))
    

