"""Suppose there is a dictionary named exam_marks as given below.
exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Write a Python program that takes an input from the user and creates a new dictionary with only
those elements from 'exam_marks' whose keys have values higher than the user input
(inclusive).
===================================================================
Sample Input 1:
170
Sample Output 1:
{'Cierra Vega': 175, 'Alden Cantrell': 200, 'Pierre Cox': 190}
===================================================================
Sample Input 2:
190
Sample Output 2:
{'Alden Cantrell': 200, 'Pierre Cox': 190}
===================================================================
"""





# solution:


user_input=int(input("Enter a num: "))

exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}

dic_={}
for key,val in exam_marks.items():
  if val>user_input:
    dic_[key]=val     # dic_ = {"Cierra":175, }

print("dicitonary is: ", dic_)


