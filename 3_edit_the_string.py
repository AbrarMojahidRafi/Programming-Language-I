"""Write a Python program that will ask the user to enter a word as an input.

If the length of the input string is less than 4, then your program should print the same string as an output.
If the input string’s length is greater than 3, then your program should add "er" at the end of the input string.
If the input string already ends with "er", then add "est" instead, regardless of the length of the input string
If the input string already ends with "est", then your program should print the same input string as an output.
=====================================================================

Sample Input 1:
strong

Sample Output 1:
stronger

Explanation: Length of input = 6, not less than 4, greater than 3, does not end with "er" or "est", therefore "er" is added making "strong", "stronger".

=====================================================================

Sample Input 2:
stronger

Sample Output 2:
strongest

Explanation: Input string ends with "er", therefore "er" is replaced with "est" instead so we have "strongest" from "stronger".

=====================================================================

Sample Input 3:
strongest

Sample Output 3:
strongest

Explanation: Our input here already ends with "est" so the same input i.e. "strongest" is printed.

=====================================================================

Sample Input 4:
abc

Sample Output 4:
abc

Explanation: Since length of input string is less than 4, the given input is printed as output.

=====================================================================

Sample Input 5:
ber

Sample Output 5:
best

Explanation: Although the length of the input string is 3 which is less than 4, but it ends with er so we ignore the length and replace "er" with "est" regardless.

=====================================================================
"""




#todo

user_input=str(input("Enter a string: "))

length=len(user_input)
if length>=4:
  if (user_input[-2]=="s" and (user_input[-3]=="e")) :
    print(user_input)
  elif (user_input[-1]!="r") and (user_input[-2]!="e") :
    print(user_input+"er")
  else: 
    print(user_input[:((length)-2)] + "est")
elif length==3 and user_input[-1]=="r" and user_input[-2]=="e":
  print(user_input[:((length)-2)] + "est")
else:
  print(user_input)