# Print a multiplication table for the number 18 up to 15. E.g. 1 x 18 = 18 2 x 18 = 36

multiplications_of = 18 # setting value to multiples of
times = 15

for loopcount in range(1, times+1): # As many times as var times.  Start at 1 and end at index times +1.
    print(str(loopcount) + " x " + str(multiplications_of) + " = " + str((loopcount * multiplications_of)))