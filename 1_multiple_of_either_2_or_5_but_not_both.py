"""
Write the Python code of a program that reads an integer, and prints the integer it is a multiple of either 2 or 5 but not both. If the number is a multiple of 2 and 5 both, then print "Multiple of 2 and 5 both". For all other numbers, the program prints "Not a multiple we want".

For example, 2, 4, 5, 6, 8, 12, 14, 15, 16, 18, 22 … i.e. this includes multiples of 2 only and multiples of 5 only, NOT multiples of 2 and 5 both or other numbers.

==========================================================

hint(1): we may use the modulus (%) operator for checking the divisibility

hint(2): we can consider the number to be an integer

==========================================================

Sample Input 1:
6

Sample Output 1:
6

==========================================================

Sample Input 2:
15

Sample Output 2:
15

==========================================================

Sample Input 3:
10

Sample Output 3:
Multiple of 2 and 5 both

==========================================================

Sample Input 4:
17

Sample Output 4:
Not a multiple we want
"""



# solution:

a=int(input("Enter some number: "))

if a%2==0 and a%5==0:
  print("Multiple of 2 and 5 both")
else: 
  print("It is a multiple of either 2 or 5 but not both")


