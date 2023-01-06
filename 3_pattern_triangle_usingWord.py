"""Write a Python program that will ask the user to input a string (containing exactly one word). Then your program should print subsequent substrings of the given string as shown in the examples below.

=====================================================================

Hints(1): You may use "for loop" for this task.

Hints(2): You may use print() function for printing newlines.

For example:
print(1)
print(2)

Output:
1
2

=====================================================================

We can use print(end = "") to skip printing the additional newline.

For example:
print(1, end ="")
print(2)

Output:(prints the following output right next to the previous one)
12

=====================================================================

Sample Input 1:
BANGLA

Sample Output 1:
B
BA
BAN
BANG
BANGL
BANGLA

Explanation: The length of the string is 6 so there are 6 lines where in each line a substring of the input string, of length equal to the line number is printed i.e. substring with only the letter "B" printed in the first line, substring "BA" of length 2 printed in the 2nd line, "BAN" length of which is 3 being printed in the 3rd line and so on.

=====================================================================

Sample Input 2:
DREAM

Sample Output 2:
D
DR
DRE
DREA
DREAM

Explanation: Simply, no of lines = length of the input string and no of letters in each line = line number.

=====================================================================
"""



#todo

user_input=str(input("Enter a string: "))

length=len(user_input)

for i in range(length) :
  for j in range(i+1) :
    print(user_input[j], end="")
  print()