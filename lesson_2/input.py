## Input
# used for inputting data from user such as a question

# define variable based on input from user as below
name=input("What is your name?\n")
print ("Hello " + name) # concatenation of String plus variable

# Set age variable and store as an integer based on input response to question
age = int(input("How old are you?\n")) # store as an integer
age_in_10_years = age + 10
print("In 10 years you will be " + (str(age_in_10_years))) # have to use casting to change age_in_10_years to a string as otherwise is an int and integers cannot be concatentated with a string 

# Ask for 1st then 2nd name and add together and print
first_name = input("What is your first name?\n")
last_name = input ("What is your last name?\n")
full_name = first_name + " " + last_name
print("Hello, " + full_name)