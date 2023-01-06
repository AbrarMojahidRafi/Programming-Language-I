"""
Write a Python code of a program that asks the user to enter ten numbers and then display the total and the average of ONLY the odd numbers among those ten numbers.
[Please do not use list for this task]

==========================================================

Sample Input 1:
1

2

3

4

5

6

7

8

9

10

Sample Output 1: The total of the odd numbers is 25 and their average is 5.0

Explanation: The total is 1 + 3 + 5 + 7 + 9 = 25 and the average is 25/5 = 5.0

==========================================================

Sample Input 2:
-20

13

-5

40

-17

10

20

-8

99

-200

Sample Output 2:

The total of the odd numbers is 90 and their average is 22.5

Explanation: The total is 90 = 13 + (-5) + (-17) + 99) and their average is 90/4 = 22.5
"""



#Todo


odd_num=0
total=0
for i in range(1,11):
  num10=int(input("Enter numbers: "))
  if num10 % 2 !=0:
    total= total + num10
    odd_num += 1 
print("The total of the odd numbers is", total, end=" " )
avg = total / odd_num
print("and their average is: ", avg)

