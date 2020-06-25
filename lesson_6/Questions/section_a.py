# Q1.
# Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green"
apple = {
    "Type": "Bramley",
    "Price": 0.39,
    "Colour": "Green"
}

# Q2
# Add the best before date to the dictionary - print the dictionary
apple["best before"] = "1st May"
print(apple)

# Q3
# Change the price to 0.41 - print the dictionary
apple["Price"] = 0.41
print(apple)

# Q4
# Set the apple to be on offer using a Boolean - print the dictionary.
apple["on offer"] = True
print(apple)

# Q5
# The offer has now expired, remove the key/value from the dictionary - print the dictionary
del(apple["on offer"])
print(apple)