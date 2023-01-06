n= int(input("Enter a value of n: "))

for i in range (n-1):    # mind it. double row হওয়াকে delete এর জন্যে এখানেই 1 minus করতে হবে। নিচের part এ করলে হবে না। 
  for j in range(i,n):             # | = এর মাধ্যমে আমরা পরবর্তীতে number 2 point emplement করেছি। 
    print("", end=" ")             # |
  for j in range(i):    # i+1 দিয়েছিলাম প্রথমে, কিন্তু এর ফলে একটি column বেশি হয়ে যাচ্ছে। তাই আমরা i+1 হতে 1 বিয়োগ করেছি। ফলে আমরা i+1-1 = i লিখেছি।
    print("*", end="")                        # | = এর মাধ্যমে আমরা পরবর্তীতে number 1 point emplement করেছি। 
  for j in range(i+1):       # | = এর মাধ্যমে আমরা পরবর্তীতে number 2 point emplement করেছি। 
    print("*", end="")       # |
  print() 

for i in range(n):
  for j in range(i+1):          # | = এর মাধ্যমে আমরা পরবর্তীতে number 1 point emplement করেছি। 
    print("", end=" ")          # |
  for j in range(i,n-1):                        # | = এর মাধ্যমে আমরা পরবর্তীতে number 2 point emplement করেছি। 
    print("*", end="")                          # | 
  for j in range(i,n):               # | = এর মাধ্যমে আমরা পরবর্তীতে number 2 point emplement করেছি। 
    print("*", end="")               # |
  print()