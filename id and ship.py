import sys
import math

#Number of tests to be run through code
print ("Enter number of tests to be run: ")
Not= int(sys.stdin.readline())
print (Not)

#check the number of test
if   Not < 1 or Not > 1000:
     print("ERROR: Incorrect NumberOfTests : ", Not)
#Function for argument
# Switcher is dictionary data type here
def id_and_ship(ip): 
    switcher = { 
        "B": "BattleShip",
        "b":"BattleShip",
        "C": "Cruiser",
        "c":"Cruiser",
        "F": "Frigate",
        "f":"Frigate",
        "D":"Destroyer",
        "d":"Destroyer"
    } 
   # be assigned as default value of passed argument
    #return nothing if no proper argument passed
    return switcher.get(ip, "nothing") 

if __name__ == "__main__":
    #for loop for no. of test case to run
      for index in range(0, Not):
           ip=input("Enter a character")
           print(id_and_ship(ip) ) #Argument passed to function and return and print the output


     

        
                
