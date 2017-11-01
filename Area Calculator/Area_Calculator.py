#This is a simple area calculator program for regular polygons.
#It prompts the user for a shape and then for the length of each side.
#It then outputs the perimeter and area to 2 decimal places.
#
#Todo: calcuate for non-regular polygons

import sys
import math

print("1. Circle")
print("2. Equilateral Triangle")
print("3. Square")
print("4. Regular Pentagon")
print("5. Regular Hexagon")
print()

# triangleSides = 3
# rectangleSides = 4
# pentagonSides = 5
# hexagonSides = 6

def areaShape():
    if shape == "1":
        area = math.pi*r*r
    elif shape == "2":
        area = math.sqrt(3)*s*s/4
    elif shape == "3":
        area = s*s
    elif shape == "4":
        area = (1/4)*(s*s)*math.sqrt(5*(5+(2*math.sqrt(5))))
    elif shape == "5":
        area = (3*math.sqrt(3))*s*s/2
    print("The area is: ", round(area,2))

def perimeterShape():
    if shape == "1":
        perimeter = 2*math.pi*r
    elif shape == "2":
        perimeter = 3*s
    elif shape == "3":
        perimeter = 4*s
    elif shape == "4":
        perimeter = 5*s
    elif shape == "5":
        perimeter = 6*s
    print("The perimeter is: ", round(perimeter,2))

shape = input("Choose a shape from the above options (1-5): ")
if shape == "1":
    r = float(input("What is the radius? "))
elif shape == "2" or "3" or "4" or "5":
    s = int(input("What is the length of the side? "))
else:
    print("Invalid input")

areaShape()
perimeterShape()
