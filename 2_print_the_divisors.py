"""Write a Python program that takes a number as input from the user and prints the divisors of that number as well as how many divisors the number has.

==========================================================

Sample Input 1:
6

Sample Output 1:
1, 2, 3, 6
Total 4 divisors.

==========================================================

Sample Input 2:
121

Sample Output 2:
1, 11, 121
Total 3 divisors.
"""



#Todo

input_num=int(input("Enter a number: "))

count=1
i=1
while i<=input_num:
  if i == input_num:                        # I am moving the comma from the last number....
    print(i, end="")
  elif input_num%i==0:                      # I check that, which number is divisors. 
    print(i, end=",")
    count+=1
  i+=1

print()                                     # I am giving a line break through this.
print("Total" , count , "divisors.")