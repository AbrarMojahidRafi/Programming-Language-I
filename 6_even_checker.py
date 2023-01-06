"""Write a function called even_checker that takes a number as an argument and prints whether
the number is even or odd inside the function.
===================================================================
Example 1:
Function Call:
even_checker(5)
Output:
Odd!!
===================================================================
Example2:
Function Call:
even_checker(2)
Output:
Even!!
"""



# solution:

a=int(input("Enter number: "))

def even_checker(a):
  if a%2==0:
    print("Even!!") 
  else:
    print("Odd!!")
    
even_checker(a)
