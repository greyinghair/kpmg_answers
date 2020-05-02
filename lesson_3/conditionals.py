## Conditional Statements
# use to run code based on Boolean (True/False)
# of an expresseion/statement
  # e.g
  # if True:
  #   print("This is always shown")
  # if False:
  #   print("This is never shown")

### the IF is always true, if when you use IF
### you are ask if something matches your IF,
### assuming it does then code is run.

# Format
#   if <expression>: 
#      <code> 
# code will only be run is the expression is True

## the  :  is crucial after the IF statement

## the code to run MUST be INDENTED 
## below the IF statement

name = "Alice"
if name == "Alice": # == means compare
  print("Hello " + name)

## everything INDENTED after the conditional
## statement will be run as part of that statement 
## as below example
## Trying changing name variable to NOT Dan then
## should only print the print statement that is
## not part of the IF statement as IF would have
## equaled FALSE as as name would NOT be Dan

name = "Dan"
if name == "Dan": # == means compare
  print("Hello " + name)
  print(name + ", I hope you are well")
print ("This is always run as not indented under IF")

## Comparators you can use as part of an IF statement

#   ==  Equal             e.g.  "Alice"=="Alice"
#   !=  Does NOT equal    e.g.  "Bob"!="Jim"
#   <   Less than         e.g.  4 < 10
#   >   Greater than      e.g.  12 > 8
#   <=  Less than or equal to   e.g. 7 <= 7
#   >=  Greater than or equals  e.g. 8 >= 5

# Change anem from Bob to Jim to see the 2nd IF NOT 
# statement in action
name = "Bob"
if name == "Bob":
  print("Hello " + name)
if name != "Bob":
  print("You are not Bob")

# Ask user for age
age = int(input ("How old are you now?\n"))
# if age is greater than or equal to 35
# then print "Jebus, you are getting old"
if age >= 35:
  print("Jebus! You are getting old")
# if age is less than 35 print something else
if age < 35:
  print("You are still just a young pup")

## ELSE, used after the IF block to run diff code
## than what would run if IF was TRUE

##  if <expression>:
##    # Will only be run if the expression is TRUE
##    <code>
##  else:
##    # Will only be run if the expression is FALSE
##    <code>

# e.g. if 1 is equal to 1 the Yes else No
# change one fo the numbers to not match the IF
# but instead match the ELSE
if 1 == 1:
  print("Yes")
else:
  print("No")

# Else Condition statement with user input
print("### User input for ELSE statement ###")
name2 = input("What's your name?\n")
if name2 == "Dan":
  print("Your name is Dan")
else:
  print("Your are NOT Dan")

### ELIF ###
# This is used within an IF statement, to in effect
# use a 2nd match staatement within the same IF run,
# before then hitting a catchall ELSE.  As soon as
# either IF/ELIF/ELSE is TRUE then non of the other
# statements are run withtin the code block

print("### User input for ELIF name statement ###")

name3 = "Bob"
if name3 == "Alice":
  print("Hello Alice")
elif name3 == "Bob":
  print("Hello Bob")
else:
  print("You must be Charlie")

print("### Another ELIF Example ###")
# Another example (order of pref is top to botton,
# when one of the elif is matched rest won't get
# processed)
age = int(input("How old are you?"))
if age <= 20:
  print("You are 20 or younger")
elif age < 30:
  print("You are between 21 and 29")
elif age == 40:
  print("You are 40")
elif age <= 0:
  print("You aren't born yet") # in case you enter zero or negative number
else:
  print("You are older than 40")

####################
### AND, OR, NOT ###
####################
# agen variable taken from above
if age > 12 and age < 20:
  print("You are a teenager")
if age < 13 or age > 19:
  print("You are NOT a teenager") 
if not (age > 12 and age < 20):
  print("You are NOT a teenager")