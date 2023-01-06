r=int(input("Enter the value of r: "))

for i in range(r):
  for j in range(i,r):
    print(" ", end="")
  for j in range(i):
    print("*" , end="")
  for j in range(i+1):
    print("*" , end="")
  print()