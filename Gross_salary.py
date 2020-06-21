import sys
import math

#Number of tests to be run through code
print ("Enter number of tests to be run: ")
Not= int(sys.stdin.readline())
print (Not)

#check the number of test
if   Not < 1 or Not > 1000:
     print("ERROR: Incorrect NumberOfTests : ", Not)
     
#define function with an argument
#logic to determine gross salary
def gross(bs):
    if  bs<1500:#if bs is less than the 1500
        hra = bs * 10 / 100
        da = bs * 90 / 100		
    else:
        hra = 500
        da = bs * 98 / 100
    gs = bs + hra + da
    print(gs)

if __name__ == "__main__":
    #for loop for no. of test case to run
   for index in range(0, Not):
           bs=int(input("Enter a Basic Salary"))
           gross(bs) #passing argument






