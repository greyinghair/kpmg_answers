# Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list.
# Find the index at which the user entered the number 99

numbers = []
count = 0

print("You will be asked to pick 10 numbers\n (one of which must be 99)\n\n")

# For 1st 10 loops
while len(numbers) != 10:
    if count == 0:
        numbers.append(int(input("Please pick a number "))) # Cast to int. (Input defaults to str)
        count += 1 # Only add count 1st as just used to change input question on 1st run
    else:
        numbers.append(int(input("Please pick your next number ")))  # Cast to int. (Input defaults to str)

# After 10 loops and if you haven't inputted 99 then end
if len(numbers) == 10 and 99 not in numbers:
    print("You have picked 10 numbers but 99 was NOT one of them. :-(")

# Else after 10 loops (ie AND 99 exists in list) go into next loop to determine position of "99"
else:
    for tempvar in range(0, (len(numbers))): # Loop from Index 0 to end of list (based on length of it)
        if numbers[tempvar] == 99: # Once 99 is found in the loop.  #  [] means INDEX position
            print("\nIndex Position of '99' is " + str(tempvar))