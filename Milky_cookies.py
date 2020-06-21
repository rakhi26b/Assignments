import sys
import math

#Number of tests to be run through code
print ("Enter number of tests to be run for T: ")
Not1= int(sys.stdin.readline())
print (Not1)

#check the number of test
if   Not1 < 1 or Not1> 1000:
     print("ERROR: Incorrect NumberOfTests : ", Not1)


# Iterative Python program to check if a string is subsequence of another string 
  
# Returns true if str1 is a subsequence of str2 
def isSubSequence(str1,str2): 
    m = len(str1) 
    n = len(str2) 
    p=len(str3)
    j = 0    # Index of str1 
    i = 0    # Index of str2 
    k=0 #index of str3
    # Traverse both str1 and str2 
    # Compare current character of str2 with  
    # first unmatched character of str1 
    # If matched, then move ahead in str1
    while j<m and i<n :
           if str1[j] == str2[i] :  
                j=j+1
           i = i + 1

    return i==n

def issub(str2,str3):
     n = len(str2) 
     p=len(str3)
     i = 0    # Index of str2 
     k=0 #index of str3
     while i<n and k<p:
                  if str3[k] == str2[i] :  
                       k=k+1
                  i=i+1
        
    # If all characters of str1 matched, then j is equal to m 
     return i==n
      
# Driver Program 
  

if __name__ == "__main__":
    #for loop for no. of test case to run
   for index in range(0, Not1):
          min=int(input())#Minutes spend in kitchen
          print(min)
          str2= input()
          str1="cookie milk" 
          str3="milk milk"
          if isSubSequence(str1,str2):
              print ("Yes")
          elif  issub(str2,str3):
              print ("Yes")
          else:
              print("No")
            
