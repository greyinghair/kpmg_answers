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
# 'secret.txt' contains a secret message. Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26. Work out what the secret message says
int


# Q4.
# Benford’s law states that the leading digits in a collection of data are probably going to be small. For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. Work out which of the files contains fake data.