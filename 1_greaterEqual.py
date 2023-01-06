"""Write the Python code of a program that reads two numbers from the user. The program should then print "First is greater" if the first number is greater, "Second is greater" if the second number is greater, and "The numbers are equal" otherwise.

==========================================================

Sample Input 1:
7
3

Sample Output 1:
First is greater

==========================================================

Sample Input 2:
-33
-3

Sample Output 2:
Second is greater

==========================================================

Sample Input 1:
11
11

Sample Output 1:
The numbers are equal"""



# solution :

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

if a>b:
  print("First is greater")
  
elif a<b:
  print("Second is greater")

else: 
  print("The numbers are equal")  