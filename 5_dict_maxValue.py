"""Write a Python program that finds the largest value with its key from a given dictionary.
[You are not allowed to use the max() function for this task]
Note: You do not need to take the dictionaries as an input from the user but your code should
work for any given dictionary. Also, you need to handle the quotation marks as a part of the
output.
Hint: Think of membership operators (in and not in). You can use dictionary functions to get the
values.
===================================================================
Sample 1:
Given:
{'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
Output:
The highest selling book genre is 'mystery' and the number of books sold are 15.
===================================================================
Sample 2:
Given:
{'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure':9}
Output:
The highest selling book genre is 'horror' and the number of books sold are 14.
===================================================================
"""



# solution:

given_dict={'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}

max_val=-9999999999999999999999999
max_keys=""

# The highest selling book genre is 'mystery' and the number of books sold are 15. 

for key,value in given_dict.items():
  if max_val<value:
    max_val=value # assign 
    max_keys=key

print(f"The highest selling book genre is '{max_keys}' and the number of books sold are {max_val}.")

print(f'The highest selling book genre is \'{max_keys}\' and the number of books sold are {max_val}.')



