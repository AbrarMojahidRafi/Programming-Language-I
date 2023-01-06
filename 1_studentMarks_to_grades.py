"""Write the Python code of a program that reads a student’s mark for a single subject, and prints out the corresponding grade for that mark. The mark ranges and corresponding grades are shown in the table below. You need to make sure that the mark is valid. For example, a student cannot receive -5 or 110 marks. So, the valid marks range is 0 to 100.

hint(1): you can consider the number to be an integer

hint(2): this problem can be solved in two ways: top-down (starts from A) and bottom-up (starts from F)

Marks	        Grade
90 or above	    A
80-89	          B
70-79	          C
60-69	          D
50-59	          E
Below 50	      F

"""


#todo


marks=int(input("Enter your marks: "))

if ((marks<0) or (marks>100)):
  print("This marks is not valid")
elif (90<= marks <=100):
  print("Your Grade is: A")
elif (80<= marks <=89):
  print("Your Grade is: B")
elif (70<= marks <=79):
  print("Your Grade is: C")
elif (60<= marks <=69):
  print("Your Grade is: D")
elif (50<= marks <=59):
  print("Your Grade is: E")
else: 
  print("Your Grade is: F")


