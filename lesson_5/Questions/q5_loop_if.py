# Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
# If they get it wrong, print "Password failure" and then ask them to enter it again.
# Only allow them to enter the password wrong 3 times before printing "System Locked!"

password = "" # Set to a str
loop_count = 0 # Set to an int

while password != "qwerty123" and loop_count < 3: # If password wrong and less than 3 attempts then loop
    password = (input(str("What is your password? "))) # Ask for password and set in variable
    if password != "qwerty123": # If wrong password
        print("Password failure")
        loop_count += 1 # Increment counter by 1 on each failure

    else: # this only hit if inverse of above is True (i.e. you entered "qwerty123" within 3 attempts)
        print("You have successfully logged in")

if loop_count >= 3: # After 3 attempts
    print("System Locked!")