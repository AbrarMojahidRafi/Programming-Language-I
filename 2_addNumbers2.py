"""Write the Python code of a program that adds all numbers that are multiples of either 7 or 9 up to 600 (including 600) i.e. 7, 9, 14, 18, 21, 27, 28, 35, 36.....
Ensure that numbers like 63, 126, 189 which are multiples of both 7 and 9 are added only once in the sum.

The output of your program should be: 42649
"""

#Todo

count=0
sum=0
while count<=600:
  if count%7==0 or count%9==0:
    sum = sum + count
  count+=1
print(sum)