"""Write a Python code of a program that adds all numbers that are multiples of either 7 or 9 but not both, up to 600 (including 600) i.e. 7, 9, 14, 18, 21..... and so on but not the numbers 63, 126, 189..... which are multiples of both 7 and 9.

The output of your program should be: 39814
"""

#Todo 

count=0
sum=0
while count<=600:
  if (count%7==0) ^ (count%9==0):   # ^ means XOR Gate. 
    sum = sum + count
  count+=1
print(sum)

