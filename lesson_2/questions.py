## Question 1
# 2 variables.  width and height of a rectangle.
# 3rd variable to work out and store the area
# Print "Rectangle of width <x> and height <y> has an area of <area>

width = 5
height = 15
area = (int(width) * (int(height)))
print(str(area))

## Question 2
# write code that prints the length of string, 'python'
  # simple version:
print (len("python"))
  # Fancy version of the above:
print("The number of characters in 'python' are, " + (str(len("python"))))

## Queation 3
# print out first and third letter of word 'python'
print("python"[0])
print("python"[2])

## Question 4
# Ask for users name and print "Hello, <name>"
name = input("What is your name?\n")
print("Hello, " + name + ".")

## Question 5
# Ask user for their age and tell them how old
# they will be in 15 years time.
age_now = (int(input("How old are you?\n")))
age_in_15_years = age_now + 15
print("In 15 years time you will be " + str(age_in_15_years) + " years old")

## Question 6
# Combine inputs ffrom Q4 & Q5 and print "Hello, <name>, you are currently <age> years old.  In 15 years time you will be <age_in_15_years> yeards old"
print("Hello, " +(name) + ", you are currently " + str(age_now) + ".  In 15 years time you will be " + str(age_in_15_years) + " yeards old.")

## Question 7
# Ask for users hometown and print it out in uppercase letters
hometown = input("What is your hometown?\n")
print("You live in, " + hometown.upper())

## Question 8
# Ask user for their favourite colour and then find out the length of said colour.
fav_colour = input("What is your favourite colour?\n")
print("There are " + str(len(fav_colour)) + " characters in " + (fav_colour))

## Question 9
# Ask user for weather and the month and print
weather = input("What is the weather like where you are?\n")
month = input("What month of the year are we in?\n")
print("It is currently " + month + " and " + weather)

## Question 10
# Ask user to enter 5 difference temperatures
# and the month.  Work out average temp and print
# as a string
month = input("What month is it?\n")
temp1 = int(input ("List 1st temp from a day in " + month + ".\n"))
temp2 = int(input ("List a 2nd temp from a day in " + month + ".\n"))
temp3 = int(input ("List a 3rd temp from a day in " + month + ".\n"))
temp4 = int(input ("List a 4th temp from a day in " + month + ".\n"))
temp5 = int(input ("List a 5th temp from a day in " + month + ".\n"))
avg_temp = (temp1+temp2+temp3+temp4+temp5)/5
print("The average temp in " + month + " was " + str(avg_temp) + " degrees.")

## Question 11
# Using above print function but make the month
# uppercase
print("The average temp in " + (month.upper()) + " was " + str(avg_temp) + " degrees.")

## Question 12
# Create a variable that holds your favourite
# animals and print it out with 1 animal per line
# and tabbed
fav_animals = ("Dog\t\nCat\t\n")
print("List of your favourite animals are:\n " + fav_animals)

## Question 13
# Ask user for their name and to choose a number.
# Print out the uppercase character at that
# position in the string
name = input("What is your name?\n")
num = int(input("Pick a number from between 0 & 3\n"))
print("The letter you chose to be uppercase was, " + name.upper()[(num)] + ".\n")