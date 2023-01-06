"""Write a function called foo_moo that takes a number as an argument and returns the following
statements according to the below mentioned conditions. Then, finally prints the statement in
the function call.
If the number is divisible by 2, it should return "Foo".
If the number is divisible by 3, it should return "Moo".
If the number is divisible by both 2 and 3, it should return "FooMoo".
Otherwise, it returns "Boo".

Example1:
Function Call:
foo_moo(5)
Output:
Boo
===================================================================
Example2:
Function Call:
foo_moo(4)
Output:
Foo
===================================================================
Example3:
Function Call:
foo_moo(6)
Output:
FooMoo
"""




user_number=int(input("Enter a number: "))

def foo_moo(n):
  if n%2==0 and n%3==0:
    return ("FooMoo")
  elif n%3==0:
    return ("Moo")
  elif n%2==0:
    return ("Foo")
  else:
    return("Boo")

ret=foo_moo(user_number)
print(ret)
