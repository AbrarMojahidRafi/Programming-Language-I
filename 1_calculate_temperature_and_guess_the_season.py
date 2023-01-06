"""You are designing a robot that can calculate the temperature and guess the season. Write a Python program that takes a number as input, representing the temperature in degrees Fahrenheit, and converts it into degrees Celsius, and then prints the season based on the following table:

Temperature (degrees Celsius)------------------------------ Season
Less than 20 degrees)--------------------------------------Winter
Between 20 degrees and 25 degrees (inclusive)--------------Autumn
Greater than 25 degrees and less than 30 degrees-----------Spring
Greater than or equal to 30 degrees------------------------Summer

Use the following formula to convert the temperature:
(degrees Celsius) = ((degrees Fahrenheit) - 32) * 0.56

==========================================================

Sample Input 1:
82

Sample Output 1:
28 degrees C
Spring

Explanation: The temperature in Celsius is (82 - 32) * 0.56 = 28 degrees, which is printed. This is between 25 and 30 degrees, so “Spring” is printed after that.

==========================================================

Sample Input 2:
32

Sample Output 2:
0 degrees C
Winter

Explanation: The temperature in Celsius is (32 - 32) * 0.56 = 0 degrees, which is printed. This is less than 20 degrees, so “Winter” is printed after that.

==========================================================

Sample Input 3:
76

Sample Output 3:
24.64 degrees C
Autumn

Explanation: The temperature in Celsius is (76 - 32) * 0.56 = 24.64 degrees, which is printed. This is between 20 degrees and 25 degrees (inclusive), so “Autumn” is printed after that.

==========================================================

Sample Input 4:
77

Sample Output 3:
25.2 degrees C
Spring

Explanation: The temperature in Celsius is (77 - 32) * 0.56 = 25.2 degrees, which is printed. This is greater than 25 degrees and less than 30 degrees, so “Spring” is printed after that.
"""

#todo

fahrenheit=int( float (input("Enter Fahrenheit: ")) )

# (degrees Celsius) = ((degrees Fahrenheit) - 32) * 0.56
celsius=((fahrenheit) - 32)*0.56
print("{:.2f} degree C".format(celsius))

if (celsius<20):
  print("Winter")

elif (20<=celsius<=25):
  print("Autumn")

elif(25<celsius<30):
  print("Spring")    

#celsius>=30
else:                         
  print("Summer")

