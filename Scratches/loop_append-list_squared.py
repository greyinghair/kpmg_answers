# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
numbers = ["5", "11", "73", "4721", "35"]
numbers_square = []
for square in numbers:
    if square:
        numbers_square.append(int(square) ** 2)
print (numbers_square)
