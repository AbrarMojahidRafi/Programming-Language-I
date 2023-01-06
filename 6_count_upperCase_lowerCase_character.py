"""Write a python function that takes a string as an argument. Your task is to calculate the number
of uppercase letters and lowercase letters and print them in the function.
===================================================================
Function Call:
function_name('The quick Sand Man')
Output:
No. of Uppercase characters : 3
No. of Lowercase Characters: 12
===================================================================
Function Call:
function_name('HaRRy PotteR')
Output:
No. of Uppercase characters : 5
No. of Lowercase Characters: 6
"""




user_input=input("Enter a string: ")

def function_name(user_inp):
  upperCase_count=0
  lowerCase_count=0
  for i in user_inp:
    if ord("a")<=ord(i)<=ord("z"):
      lowerCase_count+=1
    elif ord("A")<=ord(i)<=ord("Z"):
      upperCase_count+=1
  return lowerCase_count, upperCase_count

l,u=function_name(user_input)

print("No. of Uppercase characters:", u)
print("No. of Lowercase Characters:", l)



# function_name('The quick Sand Man')

# function_name('HaRRy PotteR')

