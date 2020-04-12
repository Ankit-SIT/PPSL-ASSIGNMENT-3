#!/usr/bin/env python3

run = True

dab = {}

while(run):
 print("\n\n\n\n\nWelcome to the Database")
 print("1. Add a contact")
 print("2. Search for a contact")
 print("3. Delete a contact ")
 print("4. Exit Program")
 choice = int(input("\n\n ENTER CHOICE: "))

 if(choice == 1):
    tName = str(input("\nNAME: "))
    tNo = int(input("\nPHONE NUMBER: ")) 

    dab.update({tName:tNo})
    print("Successfully added " + str(tName) + " as " + str(tNo))

 elif(choice == 2):
     tName = str(input("\nNAME: "))

     if(tName in dab):
      print(dab.get(tName))

     else:
      print("NO CONTACT FOUND WITH THAT NAME")
     input("\nPRESS ANY KEY TO CONTINUE") 

 elif(choice == 3):
     
     tName = str(input("\nNAME: "))

     if(tName in dab):
        del dab[tName]
     else:
       print("NO CONTACT FOUND WITH THAT NAME")  
       input("\nPRESS ANY KEY TO CONTINUE") 
 elif(choice == 4):
     run = False

 else:
    print("INVALID CHOICE!!")
  
print("EXITING PROGRAM")
