"""Assume, you have been given a tuple. Write a Python program that creates a new
tuple excluding the first and last two elements of the given tuple and prints the new tuple.
Hint: You may use tuple slicing.
===================================================================
Sample Input 1:
(10, 20, 24, 25, 26, 35, 70)
Sample Output 1:
(24, 25, 26)
===================================================================
Sample Input 2:
(-10, 20, 30, 40)
Sample Output 2:
()
===================================================================
Sample Input 3:
(-10, 20, 25, 30, 40)
Sample Output 3:
(25,)
"""




# solution:

user_input=input("enter a number: ")

s=user_input[1:-1].split(", ")

new_list=[]
for i in s:
  new_list.append(int(i))


p=new_list[2:-2] 
tup=tuple(p)
if len(new_list) <= 4:
  print("()")
else:
  print(tup)
