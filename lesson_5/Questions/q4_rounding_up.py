# The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm,
# then print the area to the whole square metre. E.g. 240cm x 80cm = 19200cm2 = 2m2

from math import ceil # Import ceiling (round up) function from math module

height = int(input("Height of a rectangle in (cm) ? "))
width = int(input("Width of rectangle in (cm) ? "))
print("The area of your square (rounded up) is " + str(ceil((height * width) / 100 / 100)) + "m2")