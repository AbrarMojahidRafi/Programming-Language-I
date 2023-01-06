"""Assume, you have been given two lists. [Your program should work for any two given lists; change the following lists and check whether your program works correctly for the code you have written]

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]

Write a Python program that creates a new list with all the even elements of both of the given lists and prints the new list.

Hint: You may create a third list to store the even elements of the given lists.

===================================================================

Output for the above lists: [2, 4, 6, 8, 10, 12, -14, -16]

===================================================================
"""




#todo

################################################################
####################### given input #############################

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]

#################################################################
#################### main work ##################################



########## 1st list 

l1=[]
for i in list_one:
  if i%2 == 0 :
    l1.append(i)

########## 2nd list  

l2=[]
for i in list_two:
  if i%2 == 0 :
    l2.append(i)
        
########## final output 

l1.extend(l2)
print(l1)