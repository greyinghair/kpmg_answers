## While loops differ from FOR loops in that FOR loops run for a fix number of loops
## WHILE loops continue to run as long as the value is True

# e.g. WHILE will keep running the loop below every time guess value does NOT equal 4.
# loop will only end once the user inputs 4.

guess = ""
while guess != 4:
    guess = int(input("Guess a number.. ")) # must set to INT or else runs indefintely as condition is never False


# next example will print Hello x10 times before condition changes to False at 10 then ends

times_in_loop = 0
while times_in_loop <= 10: # will be true until the 11th time then false so will then stop running the following code
    print("hello")
    print(times_in_loop) # shows number of loops have run through based on below
    times_in_loop = times_in_loop + 1 # Add 1 to time_in_loop value on each run


