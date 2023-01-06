"""Assume, you have been given two lists: List_one and List_two. [Your program should work for any two given lists; change the following lists and check whether your program works correctly for the code you have written]

Write a Python program that prints "True", if the given two lists have at least one common member. Otherwise, print "False".

Note: Please use concepts of flag and break to solve this task.

===================================================================

Given lists 1:
List_one : [1, 4, 3, 2, 6]
List_two : [5, 6, 9, 8, 7]

Sample Output 1:
True

===================================================================

Given lists 2:
List_one : [1, 4, 3, 2, 5]
List_two : [8, 7, 6, 9]

Sample Output 2:
False

===================================================================
"""





#todo

################################################
############### input #########################
user_input1 = input("Enter input1: ")

u=user_input1[1:-1].split(", ")
main_list1 = []
for i in u:
  main_list1.append((i))   


user_input2 = input("Enter input: ")

u=user_input2[1:-1].split(", ")
main_list2 = []
for i in u:
  main_list2.append((i))    


###############################################
############### main work #####################

flag=False


for i in main_list1:
  if i in main_list2:
    flag=True
    print(flag)
    break

    
if flag==False:
  print(flag)


  