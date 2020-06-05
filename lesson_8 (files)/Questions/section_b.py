# Section B
# Q1.
# Ask the user to enter their name and append this to a file called register.txt
file = open("register.txt","a")
name = True
while name: # Loop whilst name is true, is not empty string (ENTER) which is False
    name = input("What is your name? ")
    file.write(name + "\n") # Write results from name variable to register.txt
file.close()

# Q2.
# Create a new file called 'even.txt' that contains only the even numbers from the file 'numbers.txt'
num = open("numbers.txt","r") # Open as read mode "r"
even = open("even.txt","w") # Create/overwrite even.txt "w"
for n in num: # Loop through every line
    if int(n) % 2 == 0: # If number (cast string to int) from file is EVEN then:
        even.write(n)
num.close()
even.close()


# Q3.
# 'secret.txt' contains a secret message. Each number represents the letter of the alphabet
# where 1 = A, 2 = B ... Z = 26. Work out what the secret message says

secret = open("secret.txt","r") # will read as a STRING

for num in secret:
    if int(num) == 1: # Will be str when read from file so cast num to int
        print("A")
    elif int(num) == 2:
        print("B")
    elif int(num) == 3:
        print("C")
    elif int(num) == 4:
        print("D")
    elif int(num) == 5:
        print("E")
    elif int(num) == 6:
        print("F")
    elif int(num) == 7:
        print("G")
    elif int(num) == 8:
        print("H")
    elif int(num) == 9:
        print("I")
    elif int(num) == 10:
        print("J")
    elif int(num) == 11:
        print("K")
    elif int(num) == 12:
        print("L")
    elif int(num) == 13:
        print("M")
    elif int(num) == 14:
        print("N")
    elif int(num) == 15:
        print("O")
    elif int(num) == 16:
        print("P")
    elif int(num) == 17:
        print("Q")
    elif int(num) == 18:
        print("R")
    elif int(num) == 19:
        print("S")
    elif int(num) == 20:
        print("T")
    elif int(num) == 21:
        print("U")
    elif int(num) == 22:
        print("V")
    elif int(num) == 23:
        print("W")
    elif int(num) == 24:
        print("X")
    elif int(num) == 25:
        print("Y")
    elif int(num) == 26:
        print("Z")

secret.close()

# Q3 - kpmg way
# use a dictionary and then the numbers equate to the index position in said dict.

alphabet = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z"
}

word = "" # empty variable str so can add each letter to it
for num in open("secret.txt", "r"):
    x = int(num) # Convert num value (str) to int and place in new var called x
    word += alphabet[x]
print(word)

# Q4.
# Benford’s law states that the leading digits in a collection of data are probably going to be small.
# For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected
# probability is 11.1% (i.e. one out of nine digits). Fake data is usually evenly distributed, where as
# real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data.
# Work out which of the files contains fake data.

# Fake data likely close in values of use to those created by randomly generated baseline

import random
# Generate 1 to 9 x 10000.  Will be integer.
random_nums = (random.randint(1,9) for x in range(1, 10001))

def percentage(filename, file):
    count = {} # Empty dictionary
    lines = 0
    for x in range(1,10): # cycle through 9 times (index 10)
        count[str(x)] = 0 # set value of to 0 for keys 1 to 9.

    # Loop through 10000 randomly generated int and count how many of 1-10 there are and add to dict
    for y in file:
        if filename == "Random_Baseline":
            # Add to each dict value of 1-9 each time said number found
            count[str(y)] += 1
            # Increment lines to record number of lines for later calc
            lines += 1
        elif y:
            first_character = y[0] # Take first character (index 0) per line only
            # Add to each dict value of 1-9 each time said number found
            count[first_character] += 1
            # Increment lines to record number of lines for later calc
            lines += 1

    print(count)

    print("Results for: " + str(filename))

    # Loop through count dict and calc percentage of each value of 1-10 based on number of lines in file
    for z in count:
        # round(value,2) # rounds value to 2 decimal places
        rounded=round(((count[z] / lines) * 100),2) # # Calc % and round to 2 decimal places
        print(z + ": " + str(rounded) + "%")

    # Close file after use
    file.close()

def accounts():
    for loop in range(1,4): # Loop 3 times (1 to index 4 for the 3 x accounts files)
        filename = ("accounts_" + str(loop) + ".txt")
        file = open(filename, "r")
        percentage(filename,file) # Pass name of file for printing along with data from file to function "percentage"


accounts() # Find 1st num per line and display % of each number used over the whole file(s) for accounts_(1-3).txt
percentage(str("Random_Baseline"), random_nums) # Same thing as line above but for randomly generated num as a baseline

# accounts_2 more like the randomly generated baseline hence it is likely the fake data.