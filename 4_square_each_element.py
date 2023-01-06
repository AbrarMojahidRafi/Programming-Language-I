"""Write a Python program that turns every item of a list into its square. [Your program should work for any lists; make changes to the lists below and check whether your program works correctly]

===================================================================

Given list 1:
[1, 2, 3, 4, 5, 6, 7]

Sample Output 1:
[1, 4, 9, 16, 25, 36, 49]

===================================================================

Given list 2:
[3, 5, 1, 6]

Sample Output 2:
[9, 25, 1, 36]

===================================================================
"""




#todo

#######################################################
##################### input ###########################

user_input=input("Enter list input: ")

container = user_input[1:-1].split(", ")

l=[]
final_list=[]
for i in container:
    l.append(int(i))

#######################################################
################## output #############################


final_list=[]
for i in l:
    final_list. append(i**2)
print(final_list)
