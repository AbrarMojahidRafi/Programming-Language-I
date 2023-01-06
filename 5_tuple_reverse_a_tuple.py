"""Write a Python program to reverse a given tuple.
[You are not allowed to use tuple slicing]
===================================================================
Note: Unlike lists, tuples are immutable. So, in order to reverse a tuple, we may need to convert
it into a list first, then modify the list, and finally convert it back to a tuple.
===================================================================
Example 1:
Given tuple: ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
Output:
('h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')
===================================================================
Example 2:
Given tuple: (10, 20, 30, 40, 50, 60)
Output:
(60, 50, 40, 30, 20, 10)
"""



# solution:

given_tuple= (10, 20, 30, 40, 50, 60)

# ('h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')

conv_list=list(given_tuple)

conv_list.reverse()
print(tuple(conv_list))




# for don't use reverse, we need to create dummy list, then append the element. after that print tuple. 


