"""Write a python program that prints a square of size N using + where N will be given as input as illustrated in the examples below.

Hint: You may need to use nested loops to solve this problem.

==========================================================

Sample Input 1:

5

Sample Output 1:
+++++
+++++
+++++
+++++
+++++

Explanation: Here, we may see it as 5 rows and 5 columns, where in each horizontal row/line, 5 '+' is printed next to each other and we have a total of 5 lines.

==========================================================

Sample Input 2:

3

Sample Output 2:
+++
+++
+++

Explanation: If the input is 3, then there will be 3 rows and 3 columns, where in each horizontal row/line, '+' is printed 3 times, 1 in each of the 3 columns and we will have a total of 3 lines.
"""



#Todo

number=int(input("Enter a number: "))

for i in range(number):           
  for i in range(number):
    print("+", end="")
  print()