## Q2
# Create a Circle class, initialise it with a radius.
# Create two methods for the Circle class: get_area() and get_circumference() which give both respective areas
# and circumference, to 2 decimal places.

# Note: Area of a circle = πr ** 2
# Circumference = 2πr
# Use the round() function to get the answer to 2 decimal places

class Circle:
    pi = 3.142

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        self.area = round(self.pi * (self.radius ** 2),2)  # area is Pi * (radius squared)
        return self.area # return the calc to the call

    def get_circumference(self):
        self.circum = round(self.pi * (self.radius * 2),2)  # circum is Pi x Diameter (ie 2 x radius)
        return self.circum

radius = Circle(12) # set the radius of 12

print("The area is: " + str(radius.get_area())) # should to the calc from the radius passed above and round 2 decimal
# places
print("The circumference is: " + str(radius.get_circumference())) # calls circumference METHOD which should print the
# answer,  keep the print out of the method, use method just to calc and return value