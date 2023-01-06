"""Write the Python code of a program that adds all numbers that are multiples of both 7 and 9 up to 600 (including 600) i.e. 63, 126, 189, 252, ....

The output of your program should be: 2835
since 63 + 126 + 189 + 252 + 315 + 378 + 441 + 504 + 567 = 2835
"""


# solution:

# both 7 and 9
start=0
sum=0
while start<=600:
  if start%7==0 and start%9==0:      
    sum+=start  # sum=sum+start
  start+=1

print("sum is:", sum)

