"""Write a Python program that reads a string as an input from the user where multiple numbers are separated by spaces. Then, make a list of numbers from the input string without using the split() function and print the list. Finally, remove all the occurences of even numbers from the same input list and print the modified list.

=========================================================================

Sample Input:

7 12 4 55 96 2 11 61 33 42

Sample Output:

Original list: [7, 12, 4, 55, 96, 2, 11, 61, 33, 42]
Modified list: [7, 55, 11, 61, 33]

=========================================================================
"""




###################################################
################### input #########################

user_input=(input("Enter Input: "))

u=user_input.split(" ")

###################################################
################### 1st output ####################

my_list=[]

for i in u:
    my_list.append(int(i))
print("Oriignal list: ", my_list)

####################################################
################## 2nd output ######################

modified_list=[]
for  i in my_list:
    if int(i)%2 != 0 :
        modified_list.append(i)
print("Modified list: ", modified_list)