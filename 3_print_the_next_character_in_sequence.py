"""Write a Python program that takes a string as an input from the user containing all small letters and then prints the next alphabet in sequence for each alphabet in the input.

Hint: You may need to use the functions ord() and chr(). The ASCII value of ‘a’ is 97 and ‘z’ is 122.

=====================================================================

Sample Input 1:
abcd

Sample Output 1:
bcde

=====================================================================

Sample Input 2:
the cow

Sample Output 2:
uif!dpx

=====================================================================

[Must fulfil this criteria]

Sample Input 3:
xyzabc

Sample Output 3:
yzabcd

=====================================================================
"""





#todo

user_input=str(input("Enter a string: "))

for i in user_input:
  if i=="z":
    print("a", end="")
  else:
    variable=ord(i)
    variable+=1
    variable1=chr(variable)
    print(variable1 , end="")