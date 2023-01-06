"""Write the Python code of a program that reads two numbers, subtracts the smaller number from the larger one, and prints the result.

Hint: First, we may check which number is greater

==========================================================

Sample Input 1:
-40
-4

Sample Output 1:
36

Explanation: -4 > -40 so -4 - (-40) = -4 + 40 = 36

==========================================================

Sample Input 2:
6
2

Sample Output 2:
4

==========================================================

Sample Input 3:
5
5

Sample Output 3:
0
"""


# solution:

#todo
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

if a>b:
  c=a-b
  print(c)

else: 
  d=b-a
  print(d)

