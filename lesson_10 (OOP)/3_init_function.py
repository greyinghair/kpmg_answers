## The INIT FUNCTION is a built in function to classes.
#   __init__()
# This is always the 1st function executed when the class is being initiated into an object.

class Van:
    mirrors = 2

    def __init__(self, colour, miles):
        self.colour = colour # critical to do this
        self.miles = miles # critical to do this

    def get_mirrors(self):
        print(self.mirrors)


mercedes = Van("blue", 20000) # calls the class in variable

mercedes.get_mirrors() # 2
print(mercedes.colour) # blue
print(mercedes.miles) # 20000