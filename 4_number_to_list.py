"""
Write a Python program that reads 5 numbers from the user into a list. After reading each number, print all the numbers that have been entered so far in the list.

Example:
If the user enters 3, prints “Numbers in the list: [3]”
If the user enters 5 next, prints “Numbers in the list: [3, 5]”
If the user enters 34, prints “Numbers in the list: [3, 5, 34]”
If the user then enters -11, prints “Numbers in the list: [3, 5, 34, -11]”
Finally, if the user enters 0 as the last number, prints “Numbers in the list: [3, 5, 34, -11, 0]”
"""




# solution:


empList=[]
for i in range(5):  
  user_inp=int(input("Enter numbers: "))
  empList.append(user_inp)
  print("Numbers in the list: ",empList )



#todo

l=[]
count=1
while count<=5:
    user_input=int(input("Enter input: "))
    l.append(user_input)
    print("Numbers in the list: ", l)
    count+=1