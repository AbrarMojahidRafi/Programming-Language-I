"""Write a Python program that takes a list as an input from the user, then creates a new list excluding the first and last two elements of the given list and prints the new list. If there are not enough elements in the list to do the task, print "Not possible".

Note: You may use list slicing.

===================================================================

Sample Input 1:
[10, 20, 24, 25, 26, 35, 70]

Sample Output 1:
[24, 25, 26]

===================================================================

Sample Input 2:
[10, 20, 24, 25, 26]

Sample Output 2:
[24]

===================================================================

Sample Input 3:
[10, 20, 24, 25]

Sample Output 3:
[]

===================================================================

Sample Input 4:
[10, 20, 24]

Sample Output 4:
Not possible

===================================================================
"""



#todo

#######################################################
################## input #############################

user_input=input("Enter list input: ")

container = user_input[1:-1].split(", ")


#######################################################
################## main work ###########################

l=[]
for i in container:
    l.append(int(i))

if len(l) <= 3:
    print("Not possible")
elif len(l) == 4:
    print("[]")
else:
    print(list(l[2:-2]))