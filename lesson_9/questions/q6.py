# Q6
# Create a function that can accept a series of numbers and a mathematical operand.
# Return the result of calculating the expression. E.g.: # calculate(1, 2, 3, 4, operand = "multiply")
# calculate(65, 200, 84, 12, operand = "add")`

def calculate(*args, operand = "plus"): # set default operand if non is passed
    calc = ""
    total = args[0] # set the starting total to the 1st number in list so don;t end up subtracting or multiplying by
    # zero value
    count = 0

    for arg in args[1:]: # use index position 1 then : and blank means 1 to end. Don't want
        # to reuse value at index 0 as that has already been used in total starting position above
        if operand in ["add", "+", "plus"]: # list of possible values of keyword
            total += arg
        elif operand in ["subtract", "-", "minus"]: # list of possible values of keyword
            total -= arg
        elif operand in ["multiply", "*", "x", "times"]: # list of possible values of keyword
            total *= arg
        elif operand in ["divide", "/"]: # list of possible values of keyword
            total /= arg
        else:
            print("You have entered an invalid operand value")

    print(total)
    return total

calculate(1, 2, 3, 4, 5, operand = "add") # 15
calculate(100, 12, 13, 14, 5, operand = "subtract") # 56
calculate(100, 12, 13, 14, 5, operand = "multiply") # 1092000
calculate(1092000, 12, 13, 14, 5, operand = "divide") # 100
calculate(100, 12, 13, 14, 5, operand = "div") # Invalid Operand