"""Suppose you are given the following dictionary where the values are lists.
dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
Write a Python program that counts the total number of items in a dictionary’s values and prints
it.
[Without using sum(), len(), count() functions]
Note: Make changes to the above dictionary and see if your code works properly for other
dictionaries as well.
===================================================================
Output:
9
===================================================================
"""





# solution:

dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}

count=0
for value in dict_1.values(): # for key in dict_1:
  for i in value:             #     for i in dict_1[key]: 
    count+=1

print(count)

