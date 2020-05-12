# Print a multiplication table for the number 18 up to 15. E.g. 1 x 18 = 18 2 x 18 = 36

multiplications_of = 18 # setting value to mutliple
count = 0

while count != 15: # Run until 15 loops have completed
    count += 1 # add 1 to the count
    print(str(count) + " x " + str(multiplications_of) + " = " + str((count * multiplications_of)))