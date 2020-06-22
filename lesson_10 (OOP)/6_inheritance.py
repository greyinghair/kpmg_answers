## You have a PARENT class as well as a CHILD class
# Children inherit from Parents
# ANY Class can be a PARENT class

# Previous examples in this weeks lesson are all Parent classes so far

# To create a CHILD class you pass the PARENT class as a PARAMETER to the CHILD class
# e.g:

class Fruit:
    pass

class Apple(Fruit): # This is a CHILD class, with Van being the PARENT class passed to it
    pass

# More detailed example

class Van:
    mirrors = 2

    def __init__(self, colour, miles):
        self.colour = colour # critical to do this
        self.miles = miles # critical to do this

    def get_mirrors(self):
        print(self.mirrors)

    def van_information(self):
        print("\nThis van is " + self.colour + " and has " + str(self.miles) + " miles on the clock")

class Ford(Van):  #  Child class that uses properties of Van (parent)
    pass

ford_f50 = Ford("black", 99100) # calls the class in variable
ford_f50.van_information() # call the car_information method <object>.<method>