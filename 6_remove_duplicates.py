"""Write a function called rem_duplicate that takes a tuple in the parameter and return a tuple
removing all the duplicate values. Then print the returned tuple in the function call.
[Cannot use remove() or removed() for this task]
===================================================================
Hints:
Unlike lists, tuples are immutable, so the tuple taken as an argument cannot be modified. But
the list can be modified and lastly for returning the result use type conversion. You need to use
membership operators (in, not in) for preventing adding any duplicates values.
===================================================================
Example1:
Function Call:
rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0))
Output:
(1, 2, 3, 4, 5, 6, 0)
===================================================================
Example2:
Function Call:
rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))
Output:
('Hi', 1, 2, 3, 'a', [1, 2])
"""




# solution:

user_input=input("Enter a tuple: ")
l=user_input[1:-1].split(", ")

def rem_duplicate(l):
  newList=[]
  for i in l: 
    if i not in newList:
      newList.append(i)
  tup=tuple(newList)
  return tup
  
ansIs=rem_duplicate(l)
print(ansIs)



