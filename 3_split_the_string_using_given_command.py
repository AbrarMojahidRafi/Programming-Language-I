"""Write a python program that splits a given string on a given split character. The first input is a String and the second input is the character that will be used to split the first String.

[You cannot use the built-in split function for this task]

=====================================================================

Sample Input 1:
This-is-CSE110
-

Sample Output 1:
This
is
CSE110

Explanation: The second input which is the character '-', is used to split or divide the first input String 'This-is-CSE110' into 'This', 'is' and 'CSE110' which are printed individually in separate lines.

=====================================================================

Sample Input 2:
tom@gmail,harry@yahoo,bob@gmail,mary@gmail

,

Sample Output 2:

tom@gmail

harry@yahoo

bob@gmail

mary@gmail

=====================================================================
"""




#todo

user_input=input("Enter a string: ")
user_character=input("Enter a character: ")

for i in ( user_input.split(user_character) ):
  print(i)