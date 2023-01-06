"""Suppose, your friend is building an automated car called “Besla”. He needs to fix the programming of the car so that it runs at a proper speed. Now, write a python program that takes 2 inputs (distance in meters and time in seconds). The program should then print the velocity in kilometers per hour of that car. Also, it should print whether the car is working properly based on the following chart.

Velocity--------------------------------Information to be printed
Less than 60 km/h-----------------------Too slow. Needs more changes.
Between 60 km/h to 90 km/h--------------Velocity is okay. The car is ready!
Greater than 90 km/h--------------------Too fast. Only a few changes should suffice.
==========================================

Sample Input 1:
160000
7200

Sample Output 1:
80.0 km/h
Velocity is okay. The car is ready!

Explanation: After the conversion of distance and time, the velocity is (160/2) km/h = 80 km/h. So the velocity is okay

==========================================

Sample Input 2:
25400
3600

Sample Output 2:
25.4 km/h
Too slow. Needs more changes.

Explanation: After the conversion of distance and time, the velocity is (25.4/1) km/h = 25.4 km/h. So the speed is too slow.
"""



# todo

d=int( float(input("Enter your distance(m): ")) )
t=int(input("Enter your time(sec): "))

v=(d/t)*3.6
print("Velocity: {} km/hr".format(v))

if (v<60):
  print("Too slow. Needs more changes.")
elif (60<=v<=90):
  print("Velocity is okay. The car is ready!")

#Greater than 90 km/h
else:
  print("Too fast. Only a few changes should suffice.")

  