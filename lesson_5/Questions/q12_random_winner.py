# Ask the user to enter the names of people who entered a prize draw.
# Select a random winner and print their name.

import random

names = []
count = int(input("How many names to enter into prize draw?: ")) # choose number and store as integer

for loop_num in range(count): # loop for number of names chosen in count
    names.append(input("Please enter name of person # " + str(loop_num+1) + ": "))

#print(count) # uncomment to print value of count variable
#print(names) # uncomment to print all the name in a list

print("\n\nThe winner chosen by random = " + random.choice(names)) # Use random module to chose a name from the list