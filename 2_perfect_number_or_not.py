"""Write a Python program that takes a number as input from the user and tells if it is a perfect number or not.

Perfect Number: An integer number is said to be a perfect number if its factors, including 1 but not the number itself, sum to the number.

==========================================================

Sample Input 1:
6

Sample Output 2:
6 is a perfect number

Explanation:
6 has 4 divisors: 1, 2, 3, and 6.
If we add all factors except 6 itself, 1 + 2 + 3 = 6. The sum of the factors excluding the number itself sum up to the number therefore "6 is a perfect number" is printed.

==========================================================

Sample Input 2:
28

Sample Output 2:
28 is a perfect number

Explanation:
28 has the divisors: 1, 2, 4, 7, 14, and 28.
If we add all factors except itself we get 28, 1 + 2 + 4 + 7 + 14 = 28.

==========================================================

Sample Input 3:
33

Sample Output 3:
33 is not a perfect number

Explanation:
33 has 4 divisors: 1, 3, 11, and 33.
If we add all factors except itself, 15 = 1 + 3 + 11. The sum is not equal to the number, therefore 33 is not a perfect number.
"""


#Todo

input_num=int(input("Enter a number: "))

sum=0
i=1

while i<input_num:
  if input_num%i==0:         # Those who make "input_num% i == 0" true are the divisors.
    sum+=i                   # Then we add all divisors.
  i+=1


if sum==input_num:
  print(input_num, "is a perfect number")
else:
  print(input_num, "is not a perfect number")