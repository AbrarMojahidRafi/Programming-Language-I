"""Write a Python code for the following:

Ask the user to enter a Number, N
Display the summation of multiples of 7 up to that number (from 1 to N inclusive)
==========================================================

Sample Input 1:
50

Sample Output 1:
196

Explanation: The summation of multiples of 7 up to 50 is 7 + 14 + 21 + 28 + 35 + 42 + 49 = 196

==========================================================

Sample Input 2:
75

Sample Output 2:
385

Explanation: The summation of multiples of 7 up to 75 is 7 + 14 + 21 + 28 + 35 + 42 + 49 + 56 + 63 + 70 = 385
"""


#Todo

number=int(input("Enter a number: "))
start=0  # 0
sum=0
         # number
while start <= number:
  if start % 7==0:
    sum = sum + start 
  start += 1 
  
print(sum)