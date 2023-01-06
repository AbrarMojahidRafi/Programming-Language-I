"""Suppose you are given two dictionaries.
Now create a new dictionary "marks", merging the two dictionaries, so that the original two
dictionaries remain unchanged.
Note: You can use dictionary functions.
===================================================================
Given:
{'Harry':15, 'Draco':8, 'Nevil':19}
{'Ginie':18, 'Luna': 14}
Output:
{'Harry': 15, 'Draco': 8, 'Nevil': 19, 'Ginie': 18, 'Luna': 14}
===================================================================
Given:
{'A':90, 'B': 0}
{'C':50}
Output:
{'A': 90, 'B': 0, 'C': 50}
===================================================================
"""




# solution:

d1={'Harry':15, 'Draco':8, 'Nevil':19}
d2={'Ginie':18, 'Luna': 14}

marks={}

for k,v in d1.items():
  marks[k]=v
for k1,v1 in d2.items():
  marks[k1]=v1

print(marks)
