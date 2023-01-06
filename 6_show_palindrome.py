"""Write a function called show_palindrome that takes a number as an argument and then returns
a palindrome string. Finally, prints the returned value in the function call.
Example1:
Function Call:
show_palindrome(5)
Output:
123454321
===================================================================
Example2:
Function Call:
show_palindrome(3)
Output:
12321
"""



# solution:

number=int(input("Enter number: "))

def show_palindrome(number):
  s=""
  for i in range(1, number+1):
    s=s+str(i)
  for j in range(number-1, 0,-1):
    s=s+str(j)
  return s

string=show_palindrome(number)
print(string)

