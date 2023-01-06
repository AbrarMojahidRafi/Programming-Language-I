"""Write a Python program that will take one input from the user made up of two strings separated by a comma and a space (see samples below). Then create a mixed string with alternative characters from each string. Any leftover chars will be appended at the end of the resulting string.

Hint: For adding the leftover characters you may use string slicing.

Note: Please do not use lists for this task.

=====================================================================

Sample Input 1:
ABCD, efgh

Sample Output 1:
AeBfCgDh

Explanation: At first, the two strings divided by ", " should be separated. Then the first character of the first string 'A' is concatenated with the first character of the second string 'e' which in turn is concatenated to the second character of the first string 'B', the second character of the second string f and so on since the strings are of equal length.

=====================================================================

Sample Input 2:
ABCDENDFGH, ijkl

Sample Output 2:
AiBjCkDlENDFGH

Explanation: Here, since the length of the first string is greater than the length of the second string, after separation, the characters are concatenated alternatively as in sample input/output 1, till the length of the second string i.e. ijkl. Since, there are no more characters in the second string after that, the remaining characters if the first string i.e. ENDFGH in this case are concatenated at the end of the final string.

=====================================================================

Sample Input 3:
ijkl, ABCDENDFGH

Sample Output 3:
iAjBkClDENDFGH

Explanation: This time, the length of the second string is greater than the length of the first string therefore the first letters of the 2 strings 'i' and 'A', then the second letters 'j' and 'B' and so on are being concatenated until there are no more letters in the first shorter string following which the remaining letters i.e. ENDFGH again in this case too (this may be different for other different string inputs) are added at the end giving us the resulting output string.

=====================================================================
"""




# solution:


user_input=input("Enter two string: ")

separate_string=user_input.split(", ")

separate_string1 = separate_string[0]
separate_string2 = separate_string[1]

if( (len(separate_string1)) > (len(separate_string2)) ):
  length=len(separate_string1)
else:
  length=len(separate_string2)

i=0
j=0
final_string=""

for count in range(0, length):
  if ( i<len(separate_string1) ):
    final_string+= separate_string1[i]
  if ( j<len(separate_string2)):
    final_string+= separate_string2[j]
  i+=1
  j+=1


print(final_string)