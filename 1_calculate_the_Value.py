"""Suppose the following expressions are used to calculate the values of L for different values of S:

L=3000-(125*s*s)  if  S<100 

L=12000/(4+((s*s)/14900))  if  S≥100 

Write the Python code of a program that reads a value of S and then calculates the value of L.

==========================================================

hint(1): you can import math and use math function for making squares with math.pow(number, power) or you can simply write S ** 2.

hint(2): the value of S(user input) will be an integer

==========================================================

Sample Input 1:
120

Sample Output 1:
2416.2162162162163

Explanation: Since S (user input) given here is 120 >= 100, so L = 12000 / (4 + (120 * 120)/14900) = 2416.2162162162163

==========================================================

Sample Input 2:
3

Sample Output 2:
1875

Explanation: Since S (user input) given here is 3 < 100, so L = 3000 - 125 * 3 * 3 = 1875
"""



#todo

s=int(input("Enter a number: "))

if s<100:
  L=3000-(125*s*s)
  print("For 1st equ. the RESULT is: {}".format(L))

else: 
  L=12000/(4+((s*s)/14900))
  print("For 2nd equ. the RESULT is: {}".format(L))



