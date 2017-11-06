'''
Write a program that computes the surface area and the volume of a cone.
Radius and height are to be read from the console.

Hints:

  Surface area = pi * radius * height + pi * radius^2

  Volume = 1/3 * pi * radius^2 * height

  
  You can use the ** operator to compute the power (e.g., 2 ** 3 ==> 8)

Sample output:

  Please enter the radius: 2
  Please enter the height: 5
  The surface area is 43.982297150257104
  The volume is 20.94395102393195

'''

# pi is defined in the math module
from math import pi 

# YOUR CODE
def calculateSurfaceArea(radius, height):
    return pi * radius * height + pi * (radius ** 2)

def calculateVolume(radius, height):
    return 1 / 3 * pi * (radius ** 2) * height

# Expects the user to input integers
radius = int(input("Please enter the radius: "))
height = int(input("Please enter the height: "))
surfaceArea = calculateSurfaceArea(radius, height)
volume = calculateVolume(radius, height)
print("The surface area is", surfaceArea)
print("The volume is", volume)