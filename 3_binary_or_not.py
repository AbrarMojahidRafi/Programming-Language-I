"""Write a program that takes a string as input and prints “Binary Number” if the string contains only 0s or 1s. Otherwise, print “Not a Binary Number”.

=====================================================================

Sample Input 1:
01101101101

Sample Output 1:
Binary Number

=====================================================================

Sample Input 2:
12344ab0

Sample Output 2:
Not a Binary Number

=====================================================================

Sample Input 3:
10127490111

Sample Output 3:
Not a Binary Number

=====================================================================

Sample Input 4:
Binary Number

Sample Output 4:
Not a Binary Number

=====================================================================
"""



#todo

user_input=input("Enter something: ")

condition=True
for i in user_input:
  if (i != "1") and (i != "0") :
    condition= False 
    break
if condition== True:
  print("Binary Number")
else:
  print("Not a Binary Number")