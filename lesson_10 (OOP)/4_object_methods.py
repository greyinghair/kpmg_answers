## Objects methods.  When functions are a part of a class they are called METHODS

class Van:
    mirrors = 2

    def __init__(self, colour, miles):
        self.colour = colour # critical to do this
        self.miles = miles # critical to do this

    def get_mirrors(self):
        print(self.mirrors)

    # This is the object method
    def car_information(self):
        print("This is is " + self.colour + " and has " + str(self.miles) + " miles on the clock")

mercedes = Van("blue", 20000) # calls the class in variable

mercedes.get_mirrors() # 2
print(mercedes.colour) # blue
print(mercedes.miles) # 20000
mercedes.car_information() # call the car_information method <object>.<method>

# Can modify object properties (ie passed parameters) as below to change (from blue to red):
mercedes.colour = "Red"
print(mercedes.colour) # now it should say Red

# Can also delete an objects property:
del mercedes.colour
print(mercedes.colour) # should error with "no attribute"

