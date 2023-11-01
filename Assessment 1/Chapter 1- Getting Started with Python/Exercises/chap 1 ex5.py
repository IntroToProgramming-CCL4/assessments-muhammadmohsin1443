# Exercise 5: Compute area of Circle, Write a Python program which accepts the radius of a circle from the user and compute the area.

# Importing the math module for the value of pi π

import math 
# writing a command to make the user to enter the radius of a circle
radius=float(input("Enter the radius of the circle: "))
# enetering the formula to find the area of a circle with the given radius.
area=math.pi*radius*radius
# Using the print function to print the area of the circle
print("The area of the circle with the given radius {radius} is: ", area)
