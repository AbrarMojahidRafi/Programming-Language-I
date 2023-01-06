"""Write a function which will take 2 arguments. They are:
• Sentence
• Position
Your first task is to take these arguments as user input and pass these values to the function
parameters.
Your second task is to implement the function and remove the characters at the index number
which is divisible by the position (Avoid the index number 0 as it will always be divisible by the
position, so no need to remove the index 0 character). Finally, add the removed characters at
the end of the new string.
Return the value and then finally, print the new string at the function call.
[Cannot use remove() or removed() for this task]

Input:
"I love programming."
3
Function call:
function_name("I love programming.", 3)
Output:
I lveprgrmmngo oai.
===================================================================
Input:
"Python is easy to learn. I love python."
6
Function call:
function_name("Python is easy to learn. I love python.", 6)
Output:
Pythonis eay to earn.I lov pythn. sl eo
"""



# solution:

sentence=input("Enter a Sentence: ")
position=int(input("Enter the position number: "))

def function_name(sentence, position):
  new_str=sentence[0]
  deleted_str=""
  for i in range(1, len(sentence),1):
    if (i%position)!=0 : 
      new_str += sentence[i] 
    else: 
      deleted_str += sentence[i] 
  return new_str,deleted_str 
  
n,d=function_name(sentence, position)

ans_is = n + d
print(ans_is)

