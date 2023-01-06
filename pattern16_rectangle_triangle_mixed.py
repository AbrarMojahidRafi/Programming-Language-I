n=int(input("Enter the value of n: "))

for i in range((n-1)):
  for j in range(i,(n-1)):
    print("#", end=" ")
  for j in range(i+1):
    print(j+1,end=" ")
  for j in range(i):
    print(j+1, end=" ")
  for j in range(i,(n-1)):
    print("#", end=" ")
  print()