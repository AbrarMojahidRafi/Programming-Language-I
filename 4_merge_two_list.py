"""Suppose you have been given two lists. Write a Python program that replaces the last element of the first list with the second list. [Your program should work for any two given lists; make changes to the lists below and check whether your program works correctly]

===================================================================

Sample given lists 1:
List_one : [1, 4, 7, 5]
List_two : [6, 1, 3, 9]

Sample Output 1:
[1, 4, 7, 6, 1, 3, 9]

===================================================================

Sample given lists 2:
List_one : [1, 3, 5, 7, 9, 10]
List_two : [2, 4, 6, 8]

Sample Output 2:
[1, 3, 5, 7, 9, 2, 4, 6, 8]

===================================================================
"""




#todo

######################################################
############### code of input method #################

#*#*#*#*#*#*#*#*#*#*#*#* code for List_one 

user_input_one = input("Enter List One: ")

l = user_input_one[1:-1].split(", ")
final_list_one=[]
for i in l:
    final_list_one.append(int(i))

    
#*#*#*#*#*#*#*#*#*#*#*#* code for List_two 

user_input_two = input("Enter List Two: ")

l = user_input_two[1:-1].split(", ")
final_list_two=[]
for i in l:
    final_list_two.append(int(i))
    
####################################################### 
############### now main code start ###################

final_list_one.pop()      # I removed the last element from the 1st list. 

final_list_one.extend(final_list_two)         # Now I am adding the elements of 2nd list.

print(final_list_one)