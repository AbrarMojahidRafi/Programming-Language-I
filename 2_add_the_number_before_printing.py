"""Write a Python code that will read 5 numbers from the user. Your program should print the first number, the sum of the first 2 numbers, the sum of the first 3 numbers, and so on up to the sum of 5 numbers.

==========================================================

Sample Input 1:
1
2
3
4
5

Sample Output 1:
1
3
6
10
15

Explanation:
When the user enters 1 at first, we print 1, then
The user enters 2, (1 + 2) = 3, so our output is 3, then
The user enters 3, (3 + 3) = 6, hence our output is 6, then
The user enters 4, and we have (6 + 4) = 10, we print 10, and finally
The user enters 5, the final sum is 15 which is printed as the last output.

==========================================================

Sample Input 2:
11
-29
-3
47
50

Sample Output 2:
11
-18
-21
26
76

Explanation:
When the user enters 11 at first, we print 11, then
The user enters -29, (11 + (-29)) = -18, so our output is -18, then
The user enters -3, (-18 - 3) = -21, hence our output is -21, then
The user enters 4, and we have (-21 + 47) = 26, we print 26, and finally
The user enters 50, the final sum is (26 + 50) = 76 which is printed as the last output.
"""



#Todo

sum=0
for i in range(1,6):
  num10=int(input("Enter numbers: "))
  sum+= num10
  print(sum) 