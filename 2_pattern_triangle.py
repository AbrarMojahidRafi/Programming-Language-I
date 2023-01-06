"""Write a python program that prints a right angled triangle of height N using incrementing numbers where N will be given as input.

Hint: You may need to use nested loops. Try to think up to which point should the inner loop run.

==========================================================

Sample Input 1:
4

Sample Output 1:
1
12
123
1234

Explanation: For an input of 4, we have 4 rows/lines where in each line, the respective column number is printed sequentially up to the line/row number. So, in line number 1, we have 1 only. In line 2, 12 is printed. In line 3, we have 123 and so on.

==========================================================

Sample Input 2:
5

Sample Output 2:
1
12
123
1234
12345

Explanation: Numbers are printed sequentially up to the line number for each of the lines.
"""



#Todo

input_num=int(input("Enter a number: "))

i=1
while i<=input_num:
  j=1
  while j<=i:
    print(j, end="")
    j+=1
  print()
  i+=1