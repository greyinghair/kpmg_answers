## Recursion (function within a function)

# Factorial is a number multiplied by whole numbers down from our chosen number to 1:
# e.g. 4 being the factorial would mean "4 * 3 * 2 * 1"

def calc_function(x):
    if x == 1:
        return True # this will stop the loop when x is equal to 1
    else:
        return(x * calc_function(x - 1)) # this takes x (i.e. 4)  and multiples it by 3 (4-1) and sets x as 3 on 1st
        # loop, then keeps looping and reducing value of x by 1 each time until x is equal to 1 at which time True

number = 4

print("The factorial of a " + str(number) + " is " + str(calc_function(number))) # use variable of number which is 4
# and recurrsively call itself ie calc_function