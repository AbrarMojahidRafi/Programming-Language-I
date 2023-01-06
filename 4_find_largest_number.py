"""Write a Python program that reads a string containing 7 numbers separated by commas, then makes a list of those numbers and prints the largest number and its location or index position in the list. [You are not allowed to use the max(), sort(), sorted() function here]

[Your program should work for any given list; make changes to the list below and check whether your program works correctly]

Hint: You may assume the first input to be the largest value initially and the largest value’s location to be 0.

Note: You may need to be careful while printing the output. Depending on your code, you might need data conversion.

===================================================================

Sample Input:
"7, 13, 2, 10, 6, -11, 0"

Sample Output:
My list: [7, 13, 2, 10, 6, -11, 0]
Largest number in the list is 13 which was found at index 1.

===================================================================
"""





#todo

####################################################################
###################### input #######################################

user_input_str = input("Enter a string: ")

l = user_input_str[1:-1].split(", ")


######################################################################
############################ for My List #############################

final_list=[]
for i in l:
    final_list.append(int(i))
    
print("My list: ", final_list)


########################################################################
############### find the largest number and its index ##################

count_number=final_list[0]
for i in range(0,len(final_list)): 
    if final_list[i] >= count_number :
        count_number = final_list[i]
        
for i in final_list:
    if i == count_number : 
        index_number = final_list.index(i) 
        
print("Largest number in the list is", count_number, "which was found at index", index_number)

