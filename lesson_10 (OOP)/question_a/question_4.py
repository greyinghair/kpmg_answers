## Q4
# Create a Vehicle parent class, initialise it with, wheels, colour and a method to display all this information.
# i. Create a Tesla (or any car) child class
#       and add a method to get the miles and a method to display all this information.
# ii. Change the colour of the vehicle.
# iii. Delete the wheels.

class Vehicle:
    wheels = 4
    def __init__(self, colour, wheels):
        self.colour = colour
        self.wheels = wheels

    def information(self):
        print("number of wheels: " + str(self.wheels) + "\ncolour of car: " + self.colour)

class tesla(Vehicle):

    def __init__(self, colour, wheels, miles): # expected parameters to be passed (i.e. 3)
        super().__init__(colour, miles)
        self.wheels = wheels
        self.miles = miles

    def get_miles(self):
        print("number of miles: " + str(self.miles))

    def get_information(self): # call method information from parent followed by get_miles from this child
        print(super().information(), self.get_miles())




car = tesla("black", 6, 20000) # make variable eq child class and pass colour of car, 6 wheels and 20K miles
car.get_miles() # get mileage
car.information() # call variable which references the child class which inherit the method (information) of the parent

print("\n")

car.colour = "Blue" # change colour to BLUE
car.get_information() # get info from child (miles) and parent and verify now shows blue

# del car.wheels # delete wheels attribute
# print(car.wheels) # will error unless above line is commented out



