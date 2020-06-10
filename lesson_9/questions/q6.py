# Q6
# Create a function that can accept a series of numbers and a mathematical operand.
# Return the result of calculating the expression. E.g.: # calculate(1, 2, 3, 4, operand = "multiply")
# calculate(65, 200, 84, 12, operand = "add")`

def calculate(*args, **kwargs):
    calc = ""
    total = 0
    count = 0
    for key, value in kwargs.items():
        if value == "add":
            calc = "+"
        elif value == "subtract":
            calc = "-"
        elif value == "multiply":
            calc = "*"
        elif value == "divide":
            calc = "/"
        else:
            print("You have entered an invalid operand value")

    for nums in args:
        if calc == "+":
            total += nums
        elif calc == "-":
            if count == 0:
                total += nums # on first loop add 1st num in list to total so don't end up subtracting from zero
                count += 1
            else:
                total -= nums # on 2nd loop through start subtracting all subsequent numbers
        elif calc == "*":
            if count == 0:
                total += nums # on first loop add 1st num in list to total so don't end up multiplying by zero
                count += 1
            else:
                total *= nums # on 2nd loop through start multiplying all subsequent numbers
        elif calc == "/":
            if count == 0:
                total += nums # on first loop add 1st num in list to total so don't end up dividing by zero
                count += 1
            else:
                total /= nums # on 2nd loop through start dividing all subsequent numbers

    #print(total)
    return total

calculate(1, 2, 3, 4, 5, operand = "add") # 15
calculate(100, 12, 13, 14, 5, operand = "subtract") # 56
calculate(100, 12, 13, 14, 5, operand = "multiply") # 1092000
calculate(1092000, 12, 13, 14, 5, operand = "divide") # 100
calculate(100, 12, 13, 14, 5, operand = "minus") # Invalid Operand