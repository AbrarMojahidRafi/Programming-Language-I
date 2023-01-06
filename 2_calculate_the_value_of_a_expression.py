"""Write a Python code that will calculate the value of y if the expression of y is as follows (n is the input):

y=1**2-2**2+3**2-4**2+5**2.........+n**2 

==========================================================

Sample Input 1:
5

Sample Output 1:
15

Explanation: y = 1 - 4 + 9 - 16 + 25 = 15

==========================================================

Sample Input 2:
10

Sample Output 2:
-55

Explanation: y = 1 - 4 + 9 - 16 + 25 - 36 + 49 - 64 + 81 - 100 = -55

==========================================================

Sample Input 3:
20

Sample Output 3:
-210
"""



# solution:

#Todo

n=int(input("Enter The Value of n : ")) 

sum=0     
negative_sign=-1

for i in range(1,n+1):                   # range 
  ans=(i**2)*(-1)*negative_sign          # condition
  sum+=ans 
  negative_sign=negative_sign*(-1)       # negative sign will be change. 
print(sum) 