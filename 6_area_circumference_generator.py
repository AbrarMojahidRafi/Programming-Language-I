"""Write a function called area_circumference_generator that takes a radius of a circle as a
function parameter and calculates its circumference and area. Then returns these two results as
a tuple and prints the results using tuple unpacking in the function call according to the given
format.
[Must use tuple packing & unpacking]
===================================================================
Example1:
Function Call:
area_circumference_generator(1)
Output:
(3.141592653589793, 6.283185307179586)
Area of the circle is 3.141592653589793 and circumference is 6.283185307179586

Example2:
Function Call:
area_circumference_generator(1.5)
Output:
(7.0685834705770345, 9.42477796076938)
Area of the circle is 7.0685834705770345 and circumference is 9.42477796076938
===================================================================
Example3:
Function Call:
area_circumference_generator(2.5)
Output:
(19.634954084936208, 15.707963267948966)
Area of the circle is 19.634954084936208 and circumference is 15.707963267948966
"""




# solution:

radius=float(input("Enter Radius: "))

def area_circumference_generator(radius):
  circumference=2*3.14159265359*radius
  area=3.14159265359*radius*radius
  return circumference, area

c,a=area_circumference_generator(radius)

print("Area of the circle is", a, "and circumference is", c)

