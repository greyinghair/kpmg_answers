# Q4
# Create a function that will accept any number of parameters and save them all to a file, each on a new line.

def tofile(*args, **kwargs):
    file = open( "files/question4.txt", "w" ) # overwrite file each time so know is working
    for x in args:
        if x != "": # if args is NOT empty, ie if something is passed
            file.write(str(x) + "\n")
    for y in kwargs:
        if y != "": # If kwargs (ie key/value pairs NOT empty)
            file.write(str(y) + ": " + str(kwargs[y]) + "\n") # bring 'y' which is key, and kwargs index position of
            # y, ie loop number, aka the value.

    file.close() # close file


tofile(
    "cookies",
    "cream",
    name = "Dan",
    dob = "04/02/1980",
    current_age = 40
)