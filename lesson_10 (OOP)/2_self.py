## SELF Parameter.  self represents the instance of the class. By using the “self” keyword we can access the
# attributes and methods of the class in python. It binds the attributes with the given arguments.
# The reason you need to use self is because Python decided to do methods in a way that makes the instance
# to which the method belongs be passed automatically, but not received automatically.

class Van:
    mirrors = 2

    def get_mirrors(self):
        print(self.mirrors)

mercedes = Van() # calls the class in variable
mercedes.get_mirrors() # 2