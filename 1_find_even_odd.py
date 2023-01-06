"""
Write the Python code of a program that reads a number, and prints "The number is even" or "The number is odd", depending on whether the number is even or odd.

hint(1): we may use the modulus (%) operator to check for even or odd

hint(2): we can consider the number to be an integer

==========================================================

Sample Input 1:
7

Sample Output 1:
The number is odd

==========================================================

Sample Input 2:
10

Sample Output 2:
The number is even

==========================================================

Sample Input 3:
-44

Sample Output 3:
The number is even
"""



# solution:

#todo
a=int(input("Enter a number: "))

if a%2==0:
  print("The number is even")
else:
  print("The number is odd")