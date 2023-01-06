"""Write a python program that reads 5 numbers from the user into a list, and then prints them in the reverse order.

Hint: You may create a list to store the input numbers and then use loop to print them in reverse order

===================================================================

Sample Input:
5
-5
100
1
0

Sample Output:
Input data: [5, -5, 100, 1, 0]
Printing values from the list in reverse order:
0
1
100
-5
5

===================================================================
"""





#todo

#######################################################
##################### input ###########################

l=[]
for i in range(5):
    user_input = int(input())
    l.append(user_input)
print("Input data: ", l)

#######################################################
################## output #############################

print("Printing values from the list in reverse order: ")
l1 = l[::-1]
for i in l1:
    print(i)