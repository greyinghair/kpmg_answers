## Default Arguments
# Ability to set a default value for something if no value is otherwise entered
# below example ONLY USED when nothing is passed to hello function on the 3rd call would result in error

def hello(name):
    print("Hello " + name)

hello("Dan")
hello("Wendy")
#hello() # Blank so will error here

## Fix this by setting a default value as in below example. default if no data is entered is "random person"
# Default argument not used if parameter (value) is entered

#   parameter = <default value>
def bye(name = "random person"):
    print("Bye " + name)

bye("Dan")
bye("Wendy")
bye()

# Another example for if 2nd parameter is not passed to function to set default such as value of PI
# Area of a circle = Pi x Radius Squared
def circle_area (radius, pi = 3.14): # set default of pi (2nd parameter) as 3.14
    return pi * (radius ** 2) # return the calc when function is called

print(circle_area(12.2)) # Single parameter uses radius only, so default of pi (3.14) is used for 2nd parameter not passed
print(circle_area(12.2, 3.141592)) # Define 2nd parameter (Pi) so default not used