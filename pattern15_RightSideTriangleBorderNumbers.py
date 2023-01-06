n=int(input("Enter the value of n: "))

for i in range(n):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    if i==n-1 or j==0 or i==j:
      print(j+1, end=" ")
    else:
      print(" ", end=" ")
  print()