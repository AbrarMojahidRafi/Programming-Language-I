"""Write a Python program that takes a number and prints how many digits are in that number.
[Consider the input number to be an INTEGER.]

[You are not allowed to use len() function]

Example: If the user gives 9876, your program should print 4.

Hint: We may keep floor dividing by ten and count how many times this can be done until the number becomes 0 as illustrated below.

9876 // 10 = 987, count = 1
then, 987 // 10 = 98, count = 2
98 // 10 = 9, count = 3
9 // 10 = 0, count = 4

Done! When the number becomes 0 your loop can end giving you the count of digits, in this case for our input of 9876, 4 digits.
"""




#Todo

num=int(input("number:"))
count=0
while num>0:
  num= num // 10  
  count+=1

print(count)