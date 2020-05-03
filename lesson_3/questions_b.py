######################################
### Section-B Questions for Week 3 ###
######################################

## Question 1 ##
print("###Question 1###\n")
# Ask for the user's name, if they are called
# "Alice" print "Hello, Alice", if they are called 
# "Bob", print "You're not Bob! I'm Bob", else 
# print "You must be Charlie"

name=input("What is your name? (Alice|Bob|Other)\n")
if name == "Alice":
  print("Hello, Alice")
elif name == "Bob":
  print ("You're not Bob! I'm Bob")
else:
  print ("You must be Charlie")


## Question 2 ##
print("###Question 2###\n")
# Ask the user to enter their age
# If they are younger than 11, print "You're too young to go to this school"
# If they are between 11 and 16, print "You can can come to this school"
# If they are over 16, print 'You're too old for school"
# If they are 0, print "You're not born yet!"
age = int(input("What is your age?\n"))
if age <= 0:
  print("You're not born yet")
elif age >= 11 and age <= 16:
  print("You can come to this school")
elif age < 11:
  print("You're too young to go to this school")
else:
  print("You're too old for school")


## Question 3 ##
print("###Question 3###\n")
# Ask the user to enter the name of a month. If the user enters March/April/May: print " is in Spring", otherwise print "I don't know"
# Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February
# Ensure that when an unknown month is given it prints "I don't know"
month = input("What month is it?\n").upper() # change all characters inputted to UPPERCASE
if month == "MARCH" or month == "APRIL" or month == "MAY":
  print(month + " is in Spring")
elif month == "JUNE" or month == "JULY" or month == "AUGUST":
  print(month + " is in Summer")
elif month == "SEPTEMBER" or month == "OCTOBER" or month == "NOVEMBER":
  print(month + " is in Autumn")
elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
  print(month + " is in Winter")
else:
  print("I don't know")



## Question 4 ##
print("###Question 4###\n")
# Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers
num1=int(input("Please choose your 1st number "))
num2=int(input("Please choose a 2nd number "))
if not num1 %2 and not num2 %2: # Output of %2 if EVEN will be 1 which is False so we inverting it 
    # to make EVEN equal to True to run the 1st group of code
  print("Even")
elif num1 % 2 and num2 %2:
  print("Odd")
else:
    print(num1 + num2)

## Question 5 ##
print("###Question 5###\n")
# Your company has had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of
# over 7 years, a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who
# has a service of 3 - 5 years. Ask the user to input their current salary and years of service and print out their
# salary and their bonus or "No bonus" if they are not receiving one.
salary = int(input("What is your annual salary? "))
years_of_service = int(input("How many years have your worked for the company? "))
if years_of_service > 7:
    print("Your salary is " + str(salary) + " and your bonus will be " + str((salary / 100) * 20))
elif years_of_service > 5:
    print("Your salary is " + str(salary) + " and your bonus will be " + str((salary / 100) * 15))
elif years_of_service >= 3 and years_of_service <= 5:
    print("Your salary is " + str(salary) + " and your bonus will be " + str((salary / 100) * 10))
else:
    print("Sorry, no bonus for you!")


## Question 6 ##
print("###Question 6###\n")
# Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. If all three ages are the same, print that.



## Question 7 ##
print("###Question 8###\n")
# A school has following rules for their grading system:
# a. Above 80 – A
# b. 60 to 80 – B
# c. 50 to 60 – C
# d. 45 to 50 – D
# e. 25 to 45 – E
# f. Below 25 - F
# Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
