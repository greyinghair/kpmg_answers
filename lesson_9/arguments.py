## *ARGS (aka SPLAT)
# Useful when we don't know how many parameters to expect (such as if asking for user input),
# we can set an expected parameter in a function as *ARGS, doesn't have to be named that,
# could be *nums or *anything.  such as the bekiw:

def count_numbers(a, b, c):
    return a+b+c

#   print(count_numbers(1,2) # would error, as supplied 2 params when function expected 3, fine if used defaults in function
print(count_numbers(1,2,3)) # 6 as are 3 parameters and function expects 3

#  so you see how is not very dynamic, however if you use *<name> they can accept any number of parameters in a list format, such as below example

def nums_addition(*args):
    count = 0
    for x in args: # Reference the variable WITHOUT the * when outside of function naming
        count += x
    return count

print(nums_addition(1,2,3))
print(nums_addition(1,2,3,4,5))
print(nums_addition(1,2,3,4,5,6,99,101))

# simplify this further using the sum function
def nums_addition2(*args):
    return sum(args) # Sum of variable (expected in LIST format)

print(nums_addition2(1,2,3))
print(nums_addition2(1,5,3,4,5))
print(nums_addition2(1,923,3,4,5,6,99,101))

## Another example using *ARGS for dice roll, good reuseable bit of code for dice rolls in any games
# Call function and pass to it how many sided dice you are using and can use multiple dice as in 2nd and 3rd calls below:

from random import randint

def roll(*dice): # *args to allow multiple values from a list
    return sum(randint(1, sides) for sides in dice) # loop for as many times as there are parameters passed to function.

roll(20) # A 20 sided dice request random number between 1-20
roll(6,6) # Using 2 x 6-sided dice, so generated 2 random numbers between 1-6
roll(6,20) # a 6-sided and a 2--sided dice. random int between 1-6 as well as a random int between 1-20

print(roll(6,20,12)) # print to screen 6 sided dice roll, a 20-sided dice roll and 12-sided dice roll