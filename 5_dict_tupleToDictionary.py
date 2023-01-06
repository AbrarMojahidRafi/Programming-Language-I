"""Suppose you have been given the following list of tuples.
list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
Write a Python program that converts this list of tuples into a dictionary and then prints the
dictionary.
[You are not allowed to use set]
Hint: Think of membership operators (in and not in).
===================================================================
Output:
{'a': [1, 3, 2], 'b': [2, 1], 'c': [1]}
===================================================================
"""




# solution:

#item er    0   1     0   1    0   1      0    1    0   1     0   1
list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
# item        0          1       2           3        4          5  
     
dictionary={}

for i in list_1:   # i =========("a", 1)
  if i[0] not in dictionary:
    dictionary [i[0]] = []  # ---------------- {"a":[]}
    dictionary [i[0]].append(i[1]) # ---------{"a":[1]}
  else:
    dictionary [i[0]].append(i[1])

print(dictionary)

