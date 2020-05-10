# Import the random module
import random

# Documentation of functions for random module: https://docs.python.org/3/library/random.html

# Random float from 0.0 to 1.0
print(random.random())

# gets a random number between 1 and 10
number = random.randint(1, 10) # shows <module>.<function> (i.e. random.randint)
print(number)

##############
# To print a random students name, ie a random index number to choose an element om a list
import random

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
# Rmeber index starts at 0 and ends at one less than then number of items.  ie 0-4
index = random.randint(1,(len(students)-1)) # should work out as 1,4 so starts at 1 and ends at index position 4 ("Eve")
print(index) # shows index position number
print(students[index]) # uses the code above to print the element form the random chosen index position
print(str(students[index]) + " which is index " + str(index)) # lists the 2 above print statements together

##############
# The function 'choice', will randomly choose something from what is being queried, e.g. a list as below

import random
surnames = ["Stacey", "Ma", "Tang", "Cocker", "Clucas"]
print(random.choice(surnames)) # use 'random.choice' function to randomly choose an element from list 'surnames'
