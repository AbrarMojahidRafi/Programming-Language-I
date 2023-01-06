"""Write a function called show_palindromic_triangle that takes a number as an argument and
prints a Palindromic Triangle in the function.
[Must reuse the show_palindrome() function of the previous task]
===================================================================
Hints(1):
Need to use both print() and print( , end = " ") functions
===================================================================
Example1:
Function Call:
show_palindromic_triangle(5)
Output:
      1
    1 2 1
  1 2 3 2 1
 1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
===================================================================
Example2:
Function Call:
show_palindromic_triangle(3)
Output:
    1
  1 2 1
1 2 3 2 1

"""




# solution:

number=int(input("Enter number: "))

def show_palindrome(value):
  s=""
  for i in range(1, value+1):
    s=s+" "+str(i)
  for j in range(value-1, 0,-1):
    s=s+" "+str(j)
  print(s)

def show_palindromic_triangle(number):
  for i in range(1, number+1):
    print(" "*(number-i)*2, end=" ")
    show_palindrome(i)

show_palindromic_triangle(number)


