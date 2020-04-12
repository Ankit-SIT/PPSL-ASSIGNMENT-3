class ComplexNumber:
     def __init__(self, realPart, imaginaryPart):
             self.r = realPart
             self.i = imaginaryPart
     
     def CPrint(self):
      print(str(self.r) + " + " + str(self.i) + "i")

run = True

while(run):
    print("\n\n1. ADD NUMBER")
    print("2. DISPLAY NUMBER")
    print("3. EXIT")
    choice = int(input("\n\nENTER CHOICE: "))

    if(choice == 1):
         real = int(input("ENTER REAL PART: "))
         imaginary = int(input("ENTER REAL PART: "))

         c = ComplexNumber(real,imaginary)
    elif(choice == 2):
         print("THE COMPLEX NUMBER IS: ",end='')
         c.CPrint()
    
    elif(choice == 3):
        run = False
    
    else:
         print("Wrong Input")

print("EXITING PROGRAM")
