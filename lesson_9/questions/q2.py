# Q2
# Create a function that takes the circumference of a circle and return the radius and area.


def calc(circumference, pi = 3.142):
    # radius = circumference / (2 * pi)
    # area = pi * (radius ** 2)
    # print("Radius: " + str(radius.__round__(2)) + " cm") # round to 2 decimal places
    # print("Area: " + str(area) + " cm2") # round to 2 decimal places
    return circumference / (2 * pi) , pi * ((circumference / (2 * pi)) ** 2) # 2 value, 1st being radius, 2nd being area

calc(15, 3.14159265) # define overriding pi value
calc(15) # just circumference, no pi value so uses default