"""Write a Python code for the following:

1) Ask the user to enter the name of his favorite car.
2) Ask the user to enter a Number

Display the name of the user’s favorite car, the number of times specified in the second step.

==========================================================

Example 1: If the user enters “Toyota” and 2, your program should print the name “Toyota” two times.

Sample Input 1:
Toyota
2

Sample Output 1:
Toyota
Toyota

==========================================================

Example 2: If the user enters “Veyron” and 5, your program should print the name “Veyron” five times.

Sample Input 2:
Veyron
5

Sample Output 2:
Veyron
Veyron
Veyron
Veyron
Veyron

"""

# solution:

car=input("Enter your favourite car: ")
num=int(input("Enter a number: "))

start=1
while start<=num:
  print(car)
  start+=1