"""Write a python function that will perform the basic calculation (addition, subtraction,
multiplication and division) based on 3 arguments. They are:
Operator ('+', '-', '/', '*')
First Operand (any number)
Second Operand (any number)
Your first task is to take these arguments as user input and pass the values to the function
parameters.
Your second task is to write a function and perform the calculation based on the given operator.
Then, finally return the result in the function call and print the result.
=====================================================
Input:
"+"
10
20
Function Call:
function_name("+", 10, 20)
Output:
30.0
================================
Input:
"*"
5.5
2.5
Function Call:
function_name("*", 5.5, 2.5)
Output:
13.75
"""



# solution:

operator=input("Enter Operator: ")
firstNumber=float(input("Enter 1st number: "))
secondNumber=float(input("Enter 2nd number: "))

def function_name(operator, firstNumber, secondNumber):
  if operator=="+":
    add = (firstNumber + secondNumber)
    return add
  elif operator=="-":
    if firstNumber > secondNumber:
      sub1 = (firstNumber + secondNumber)
      return sub1
    elif secondNumber > firstNumber:
      sub2 = (firstNumber + secondNumber)
      return sub2
  elif operator=="*":
    mul = firstNumber * secondNumber 
    return mul
  elif operator=="/":
    divide = firstNumber / secondNumber
    return divide
    
returnResult=function_name(operator, firstNumber, secondNumber)
print(returnResult)

