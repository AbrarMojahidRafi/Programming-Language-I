"""Write a Python program that removes all Empty strings from a given list and prints the modified list. [Your program should work for any given list; make changes to the list below and check whether your program works correctly]

=========================================================================

Given List:

["hey", "there", "", "what's", "", "up", "", "?"]

Sample Output:

Original List: ['hey', 'there', '', "what's", '', 'up', '', '?']

Modified List: ['hey', 'there', "what's", 'up', '?']

==========================================================================
"""




#todo

given_list = ["hey", "there", "", "what's", "", "up", "", "?"]

print("Original List: ",given_list)


final_list = []
for i in range( 0,len(given_list) ):
    if ( len( given_list[i] ) ) > 0 : 
        final_list.append( given_list[i] )
        
print("Modified List: ",final_list)