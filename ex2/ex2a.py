#####################################################################
# FILE: ex2a.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex2 2014-2015
# DESCRIPTION:
# A simple program that asks for a shape from the user represented
# by 3 numbers. It will then ask for defining parameters for the
# shape chosen and print an Area and Perimeter of the shape to the
# output (screen)
#####################################################################
import math


shape = input("Choose a shape:")
# input is positive but not necessarily whole

if shape == '1':
    # This will ask for 2 sides of the rectangle and then print
    # it's Area and Perimeter
    width = float(input("width:"))
    height = float(input("height:"))
    
    area = width * height
    perimeter = 2*width + 2*height
    
    print("area:", area)
    print("perimeter:", perimeter)
    
elif shape == '2':
    # This will ask for the radius of the circle and then print
    # it's Area and Perimeter
    radius = float(input("radius:"))
    
    area = math.pi * (radius**2)
    perimeter = math.pi * 2 * radius
    
    print("area:", area)
    print("perimeter:", perimeter)


elif shape == '3':
    # This will ask for 3 sides of the triangle and then print
    # it's Area and Perimeter
    side_a = float(input("a:"))
    side_b = float(input("b:"))
    side_c = float(input("c:"))

    # calculate it using Heron's formula
    perimeter = side_a + side_b + side_c
#    print (perimeter)
    semi = perimeter/2   # this is the semi-perimeter in Heron's formula   
    area = math.sqrt(semi*(semi - side_a)*(semi - side_b)*(semi - side_c))
    
    print("area:", area)
    print("perimeter:", perimeter)

else:
    print("Please enter a valid number for shape: 1 for rectangle,",
                "2 for circle, or 3 for triangle")
    
