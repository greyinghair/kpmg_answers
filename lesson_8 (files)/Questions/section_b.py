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

# Q4.
# Benford’s law states that the leading digits in a collection of data are probably going to be small.
# For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected
# probability is 11.1% (i.e. one out of nine digits). Fake data is usually evenly distributed, where as
# real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data.
# Work out which of the files contains fake data.