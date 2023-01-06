"""Write a python function that takes the limit as an argument of the Fibonacci series and prints till
that limit.
===================================================================
Function Call:
fibonacci(10)
Output:
0 1 1 2 3 5 8
===================================================================
Function Call:
fibonacci(5)
Output:
0 1 1 2 3 5
"""




# solution:

limit = int(input("Enter limit: "))

def fibonacci(limit):
  a=0
  b=1
  for i in range(limit+1):
    if i <2:
      print(i, end=" ")
    else:
      sum=a+b
      a=b
      b=sum
      if sum<= limit:
        print(sum, end=" ")

fibonacci(limit)


