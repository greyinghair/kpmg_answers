######################################
### Section-A Questions for Week 3 ###
######################################

## Question 1 ##
print("###Question 1###\n")
# Ask for the user's name, if they are called "Bob", print "Welcome Bob!"

name = input("What is your name?\n")
if name == "Bob":
  print("Welcome Bob!\n")


## Question 2 ##
print("###Question 2###\n")
# Ask for the user's name, if they are not called "Alice", print "You're not Alice!"

name2 = input("What is your name?\n")
if name2 != "Alice":
  print("You're not Alice!\n")


## Question 3 ##
print("###Question 3###\n")
# Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure"

password = input("Choose a password:\n")
if password == "qwerty123":
  print("You have successfully loggd in")
else:
  print("Password failure")


## Question 4 ##
print("###Question 4###\n")
# Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd"

number = int(input("Please choose a number between 1 & 10\n"))
if number % 2: # will give 1 if odd and 0 if even.  Python see's 0 = False wherease 1 = True.  Modulas operator.
  print("Odd")
else:
  print("Even")



## Question 5 ##
print("###Question 5###\n")
# Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
pontoon1 = int(input("Pick a number:\n"))
pontoon2 = int(input("Pick a 2nd number:\n"))
pontoontotal = (pontoon1 + pontoon2)
if pontoontotal > 21:
  print("Bust")
else:
  print("Safe")

## Question 6 ##
print("###Question 6###\n")
# Ask the user to enter the length and width of a shape and check if it is a square or not.
x = int(input("What is the length of x-axis of your shape?\n"))
y = int(input("What is the length of y-axis of your shape?\n"))
if x == y:
  print("Your shape IS a Square")
else:
  print("Your shape is NOT a Square")

## Question 7 ##
print("###Question 7###\n")
# Your company has had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

salary = int(input("What is your annual salary?\n"))
years = int(input("How many years of service do you have?\n"))
if years > 3:
  print("Your salary is £" + (str(salary)) + " and your bonus will be £" + (str(salary / 10)))


## Question 8 ##
print("###Question 8###\n")
# Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
num=int(input("Choose a number either negative or positive\n"))
if num >= 0:
  print(num * num)
else:
  print(num / 2)