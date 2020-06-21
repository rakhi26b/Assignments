import sys
import math

#Number of tests to be run through code
print ("Enter number of tests to be run: ")
Not= int(sys.stdin.readline())
print (Not)

#check the number of test
if   Not < 1 or Not > math.pow(10,5):
     print("ERROR: Incorrect NumberOfTests : ", Not)


for i in range(0,Not):
    c=int(input())#input for no. of cats
    d=int(input())#input for no. of dogs
    l=int(input()) #input for no.of legs 
    if l%4==0:
      if c<=2*d:#max 2 cats can ride on dogs
        if l>=4*d and l<=(c+d)*4:
          print("yes")
        else:
          print("no")
      elif c>2*d:#if more than 2 cats exsist
        if l>=(d+c-2*d) and l<=4*(c+d):
          print("yes")
        else:
          print("no")
    else:
      print("no")

