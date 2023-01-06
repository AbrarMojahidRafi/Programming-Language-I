"""Write a Python program that takes a dictionary as an input from the user and then prints the
average of all the values in the dictionary.
[You are not allowed to use len() and sum()]
===================================================================
Hint (1): For taking dictionary input
Approach (1): For taking dictionary as an input from the user, you may take the whole dictionary
as a string using the input() function. Then you can use the split(), strip() functions and
conditions to get the keys and values from the string. Finally, you can make the dictionary using
the obtained data.
Approach (2): If the first approach seems too difficult you can create an empty dictionary and
then just run a simple loop. For each iteration ask the user for a key and a value using the
input() function and keep updating the dictionary with the key and value.
Hint (2): After you have a dictionary, you can use dictionary functions to get all the values from
it, run loop to calculate the sum and the total number of values in the dictionary in order to find
out the average.

===================================================================
Sample Input 1:
{'Jon': 100, 'Dan':200, 'Rob':300}
Sample Output 1:
Average is 200.
===================================================================
Sample Input 2:
{'Jon': 100, 'Dan':200, 'Rob':30, 'Ned':110}
Sample Output 2:
Average is 110.
===================================================================
"""




# solution:

lenght=int(input("Enter a number: "))

d={}
for i in range(lenght):
  key=input("enter a key: ")
  val=input("Enter a val: ")
  d[key]=val
print("dictionary is: ",d)


a=d.values()
count=0
for i in a:
  count+= int(i)

avg=(count//(lenght))
print(f"Average is {avg}.")