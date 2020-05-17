# Rewrite question B8 from session 3 using a while loop:
# Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list

numbers = [22, 11, 35, 78, 46]
squared = [] # Create empty list
count = 0

while count < len(numbers): # pull each element out of list and put into intermediate var called "x"
    count += 1 # Increment count
    squared.append(numbers[count - 1] ** 2) # Squared the index of 1 element on each loop and append to "squared" list

print("Your numbers squared were: " + str(squared)) # After finished looping through all elements print results