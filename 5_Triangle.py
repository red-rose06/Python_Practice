'''Program to find accept base and perpendicular and 
find hypotenuse of a right angeled triangle.'''

import math

print("Enter details of the right angeled triangle: ")

b=int(input("Enter value of base: "))
h=int(input("Enter value of perpendicular: "))

s = math.sqrt(b*b+h*h)

print(f"The third side is {s} units")