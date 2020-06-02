# Returning is useful when want to pass parameter(s) to a function but not print to screen but reuse
# e.g. calculate an area but don't print to screen

### START Example

def area(x, y, z): # function called "area" to expect 3 parameters passed which then are used in variables
    return x * y * z # calculate area but don't print, return data from function.

cube1 = area(12,16,3) # calls the function above to calculate area of the 3 x parameters and put in var called "cube1"
cube2 = area(9452,2356,14)

### END Example


### START Example

def is_odd(number):
    if number % 2: # True i.e. equals = 1 (0 is False / 1 is True)
        return True
    else:
        return False

### END Example
