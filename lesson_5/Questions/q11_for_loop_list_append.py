# Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list

numbers = [22, 11, 35, 78, 46]
squared = [] # Create empty list

for x in numbers: # pull each element out of list and put into intermediate var called "x"
    squared.append(x ** 2) # Squared the element on each loop and append to "squared" list

print("Your numbers squared were: " + str(squared)) # After finished looping through all elements print results