"""Write a Python program which takes a number and prints the digits from the unit place, then the tenth, then hundredth, etc. (Right to Left)

[Consider the input number to be an INTEGER. You are not allowed to use String indexing for solving this task]

Example: If the user gives 32768, then print 8, 6, 7, 2, 3

=========================================================================

Hint (1): The input() function, converts the input data to String data type by default. Therefore, please type cast it to an integer before proceeding further.

Hint (2): First to get the digit from the right side, we can take the remainder of the number using modulus (%) operator i.e. mod 10 to get the rightmost digit and print it. For dropping the last digit, we can perform floor division by 10 on the number and then continue the same to print the other digits as shown below.

32768 % 10 = 8

32768 // 10 = 3276

Then,

3276 % 10 = 6

3276 // 10 = 327

and so on

327 % 10 = 7

327 // 10 = 32

32 % 10 = 2

32 // 10 = 3

3 % 10 = 3

3 // 10 = 0

Done! When the number becomes 0 you can end your loop.
"""



#Todo

num=int(input("number:"))

while True:
  if num != 0 : 
    last_part= num %10             # as a result, we get the last digit.  
    print(last_part, end=",")      # That last digit will be printed and comma will sit with it. 
    num= num // 10                 # We get the part before the decimal part.  
    if num//10==0:                 # Now being 0 means all digit counts are done. 
      break
print(num) 