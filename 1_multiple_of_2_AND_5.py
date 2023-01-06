"""Write the Python code of a program that reads an integer, and prints the integer if it is a multiple of 2 AND 5 and prints "Not multiple of 2 and 5 both" otherwise.

==========================================================

For example, 10, 20, 30, 40, 50 … i.e. this only includes numbers which are multiples of both 2 and 5.

hint(1): we may use the modulus (%) operator for checking the divisibility

hint(2): we can consider the number to be an integer

==========================================================

Sample Input 1:
30

Sample Output 1:
30

==========================================================

Sample Input 2:
15

Sample Output 2:
Not multiple of 2 and 5 both

==========================================================

Sample Input 3:
6

Sample Output 3:
Not multiple of 2 and 5 both
"""



# solution:

a=int(input("Enter a number: "))

if a%2==0 and a%5==0:
  print("It is a multiple of 2 AND 5 ")
else:
  print("Not multiple of 2 and 5 both")


