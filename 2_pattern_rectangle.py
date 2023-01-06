"""Write a python program that prints a rectangle of size M (height/line numbers) and N (length/column numbers) using incrementing numbers where M and N will be given as input. Please look at the examples below for clarification.

Hint: You may need to use nested loops and print the loop counter variable in one of the loops.

==========================================================

Sample Input 1:
4
6

Sample Output 1:
123456
123456
123456
123456

Explanation: The user has given 4 rows/lines and 6 columns as input. Therefore, we have 4 lines in our output here and in each line, the column number is printed from 1 through to 6 for the 6 columns.

==========================================================

Sample Input 2:
3
2

Sample Output 2:
12
12
12

Explanation: Our user input this time is 3 rows/lines and 2 columns. So, our output has 3 lines and in each line, the column number 1 and 2 are printed next to each other as the user only wants 2 columns here.
"""


#Todo

row=int(input("Enter Row: "))
column=int(input("Enter Column: "))

i=1
while i<=row:
  j=1
  while j<=column:
    print(j, end="")
    j+=1
  print()
  i+=1