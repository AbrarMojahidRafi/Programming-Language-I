l=int(input("Enter the length: "))
w=int(input("Enter the weight: "))

for i in range(l):
  for j in range(w):
    if i==0 or j==0 or i==l-1 or j==w-1 : 
      print("*", end=" ")
    else:
      print(" " , end=" ")
  print()