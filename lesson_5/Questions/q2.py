# Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!"
number = 0
while number != 7: # As long as not 7 then keep looping (7 is INT hence no quotes)
    number = int(input("Pick a number..")) # MUST cast to integer or else is str and while statement is never False
    print("You chose " + str(number))
print("Wow lucky number 7!")