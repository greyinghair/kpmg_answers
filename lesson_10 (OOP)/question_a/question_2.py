## Q2
# Create a Circle class, initialise it with a radius.
# Create two methods for the Circle class: get_area() and get_circumference() which give both respective areas
# and circumference, to 2 decimal places.

# Note: Area of a circle = πr ** 2
# Circumference = 2πr
# Use the round() function to get the answer to 2 decimal places

class Circle:

    def __init__(self, radius):
        pi = 3.142
        self.area = pi * (radius ** 2) # area is Pi * (radius squared)
        self.circum = pi * (self.area * 2)  # circum is Pi x Diameter (ie 2 x radius)

    # def truncate(self):
    #     round(self.area,2)

    def get_area(self):
        print("\nArea is " + str(round(self.area, 2)))

    def get_circumference(self):
        print("Circumference is " + str(round(self.circum, 2)))

radius = Circle(12) # set the radius of 12

radius.get_area() # should to the calc from the radius passed above and round 2 decimel places
radius.get_circumference() # calls circumference METHOD which should print the answer