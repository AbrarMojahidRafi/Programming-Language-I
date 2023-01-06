"""Write a Python program that takes a String as input from the user, removes the characters at even index and prints the resulting String in uppercase without using the built-in function upper().

=====================================================================

Sample Input 1:

String

Sample Output 1:

TIG

Explanation: The characters 'S', 'r' and 'n' are at index positions 0, 2, and 4 respectively. Hence they are removed and the remaining characters 'tig' are capitalized giving us output 'TIG'.

=====================================================================

Sample Input 2:

abcd

Sample Output 2:

BD

Explanation: Only the characters at the odd indices, 1 and 3, 'b' and 'd' are captitalized, concatenated and printed.

=====================================================================
"""




# solution:
user_input=input("Enter a string: ")
length=len(user_input)   

# we start while loop
user_input_index=0
while user_input_index < length : 
  if user_input_index % 2 != 0 :
    a=user_input_index                  
    b=user_input[user_input_index]
    c=ord(b)
    d = c-32
    e=chr(d)
    print(e, end="")
  user_input_index += 1