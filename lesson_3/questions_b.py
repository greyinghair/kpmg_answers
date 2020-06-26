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
if num1 % 2 == 0 and num2 % 2 == 0: # Output of %2 if EVEN will be 0 (true), to signify no remainder.
  print("Even")
elif num1 % 2 == 1 and num2 % 2 == 1:
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
    print("Your salary is " + str(salary) + " and your bonus will be " + str((salary / 100) * 20)) # or you could * 0.2 instead to be more efficient
elif years_of_service > 5:
    print("Your salary is " + str(salary) + " and your bonus will be " + str((salary / 100) * 15)) # or you could * 0.15 instead to be more efficient
elif years_of_service >= 3 and years_of_service <= 5:
    print("Your salary is " + str(salary) + " and your bonus will be " + str((salary / 100) * 10)) # or you could * 0.1 instead to be more efficient
else:
    print("Sorry, no bonus for you!")


## Question 6 ##
print("###Question 6###\n")
# Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. If all three ages are the same, print that.
name1 = input("What is person #1's name? ")
age1 = int(input("What is the age of " + name1 + "? "))
name2 = input("What is person #2's name? ")
age2 = int(input("What is the age of " + name2 + "? "))
name3 = input("What is person #3's name? ")
age3 = int(input("What is the age of " + name3 + "? "))
if age1 == age2 and age2 == age3:
    print(name1 + ", " + name2 + ", and " + name3 + " are all the same age")
elif age1 > age2 and age2 > age3:
    print(name1 + " at " + str(age1) + " is the oldest, whilst " + name3 + " at " + str(age3) + " is the youngest")
elif age1 > age3 and age3 > age2:
    print(name1 + " at " + str(age1) + " is the oldest, whilst " + name2 + " at " + str(age2) + " is the youngest")
elif age2 > age1 and age1 > age3:
    print(name2 + " at " + str(age2) + " is the oldest, whilst " + name3 + " at " + str(age3) + " is the youngest")
elif age2 > age3 and age3 > age1:
    print(name2 + " at " + str(age2) + " is the oldest, whilst " + name1 + " at " + str(age1) + " is the youngest")
elif age3 > age1 and age1 > age2:
    print(name3 + " at " + str(age3) + " is the oldest, whilst " + name2 + " at " + str(age2) + " is the youngest")
elif age3 > age2 and age2 > age1:
    print(name3 + " at " + str(age3) + " is the oldest, whilst " + name1 + " at " + str(age1) + " is the youngest")


# Or another way for same result, but neater.
# Split the function of findout oldest vs youngest
# 2 x IF's needed or else on 1st match would stop processing any other ELIF's

# Oldest
if age1 > age2 and age1 > age3:
  print(name1 + " at " + str(age1) + " is the oldest.")
elif age2 > age1 and age2 > age3:
  print(name2 + " at " + str(age2) + " is the oldest.")
elif age3 > age1 and age3 > age2:
  print(name3 + " at " + str(age3) + " is the oldest.")
else:
  print(name1 + ", " + name2 + ", and " + name3 + " are all the same age")

# Youngest
if age1 < age2 and age1 < age3:
  print(name1 + " at " + str(age1) + " is the youngest.")
elif age2 < age1 and age2 < age3:
  print(name2 + " at " + str(age2) + " is the youngest.")
elif age3 < age1 and age3 < age2:
  print(name3 + " at " + str(age3) + " is the youngest.")

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
lessonname1 = input("What is Lesson #1? ")
lessonmark1 = input("What mark did you get (0-100) for " + lessonname1 + "? ")
lessonname2 = input("What is Lesson #2 ")
lessonmark2 = input("What mark did you get (0-100) for " + lessonname2 + "? ")
lessonname3 = input("What is Lesson #3? ")
lessonmark3 = input("What mark did you get (0-100) for " + lessonname3 + "? ")

# Lesson-1
if int(lessonmark1) < 25:
    print("For " + lessonname1 + " your grade was - F" )
elif int(lessonmark1) < 46:
    print("For " + lessonname1 + " your grade was - E" )
elif int(lessonmark1) < 51:
    print("For " + lessonname1 + " your grade was - D" )
elif int(lessonmark1) < 61:
    print("For " + lessonname1 + " your grade was - C" )
elif int(lessonmark1) < 81:
    print("For " + lessonname1 + " your grade was - B" )
elif int(lessonmark1) > 80:
    print("For " + lessonname1 + " your grade was - A" )

# Lesson-2
if int(lessonmark2) < 25:
    print("For " + lessonname2 + " your grade was - F")
elif int(lessonmark2) < 46:
    print("For " + lessonname2 + " your grade was - E")
elif int(lessonmark2) < 51:
    print("For " + lessonname2 + " your grade was - D")
elif int(lessonmark2) < 61:
    print("For " + lessonname2 + " your grade was - C")
elif int(lessonmark2) < 81:
    print("For " + lessonname2 + " your grade was - B")
elif int(lessonmark2) > 80:
    print("For " + lessonname2 + " your grade was - A")

# Lesson-3
if int(lessonmark3) < 25:
    print("For " + lessonname3 + " your grade was - F")
elif int(lessonmark3) < 46:
    print("For " + lessonname3 + " your grade was - E")
elif int(lessonmark3) < 51:
    print("For " + lessonname3 + " your grade was - D")
elif int(lessonmark3) < 61:
    print("For " + lessonname3 + " your grade was - C")
elif int(lessonmark3) < 81:
    print("For " + lessonname3 + " your grade was - B")
elif int(lessonmark3) > 80:
    print("For " + lessonname3 + " your grade was - A")