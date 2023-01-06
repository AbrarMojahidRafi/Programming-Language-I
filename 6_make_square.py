"""Write a function called make_square that takes a tuple in the parameter as a range of numbers
(starting point and ending point (included)). The function should return a dictionary with the
numbers as keys and its squares as values.
===================================================================
Hints:
You need to declare a dictionary to store the result. You should use the range function to run
the “for loop”.
===================================================================
Example1:
Function Call:
make_square((1,3))
Output:
{1: 1, 2: 4, 3: 9}
===================================================================
Example2:
Function Call:
make_square((5,9))
Output:
{5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
"""




# solution:

user_input=input("Enter a tuple: ")
l=user_input[1:-1].split(",")
li=[]
for i in l:
  li.append(int(i))

new_list=[]
for i in range(li[0],li[1]+1):
  new_list.append(i)

def make_square(new_list):
  d={}
  for i in new_list:
    d[i]=i**2
  return d

dictionary=make_square(new_list)
print(dictionary)

