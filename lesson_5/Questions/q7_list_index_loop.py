# Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list.
# Find the index at which the user entered the number 99

numbers = []
count = 0
x = 0
index_position = []

print("You will be asked to pick 10 numbers\n (one of which must be 99)\n\n")

# For 1st 10 loops
while len(numbers) != 10:
    if count == 0:
        numbers.append(input("Please pick a number "))
        count += 1
    else:
        numbers.append(input("Please pick your next number "))

# After 10 loops and if you haven't inputted 99 then end
if len(numbers) == 10 and "99" not in numbers:
    print("You have picked 10 numbers but 99 was NOT one of them. :-(")

# Else after 10 loops (ie AND 99 exists in list) go into next loop to determine position of "99"
else:
    for tempvar in range(0, (len(numbers))): # Loop from Index 0 to end of list (based on length of it)
        if numbers[tempvar] == "99": # Once 99 is found in the loop: (WHY [] needed ?????)
            index_position.append(tempvar) # Append how many loops ran to list which = same value as index
            print("\nIndex Position of '99' is " + str(index_position))



