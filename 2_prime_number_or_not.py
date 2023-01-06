"""Write a Python program that asks the user for one number and tells if it is a prime number or not.

Prime Number: If a number has only two divisors, (1 and itself), then it is a prime number. If it is divisible by more numbers, then it is not a prime.

Hint: You may use the code for counting divisors from Task 14.

==========================================================

Sample Input 1:
11

Sample Output 1:
11 is a prime number

Explanation: 11 has only 2 divisors: 1 and 11.

==========================================================

Sample Input 2:
6

Sample Output 2:
6 is not a prime number

Explanation: 6 has 4 divisors: 1, 2, 3 and 6
"""



#Todo

input_num=int(input("Enter a number:"))

#################################################################################
### We continue the loop from here, to check how many divisors it has in total... 

count=0
i=1
while i<=input_num:
  if input_num%i==0:
    count+=1
  i+=1

# The total number of divisors is known... 
#################################################################################


##################################################################################
################# Now we say that it is prime or not.... ########################
if count>2: 
  print(input_num, "is not a prime number")
else:
  print(input_num, "is a prime number")