# Q1
# Write a function that prints your name
def q1():
    print("Dan\n")

q1()

# Q2
# Write a function that accepts a name as a parameter and prints "Hello, "

def q2(name):
    print("Hello, " + name)

q2("Dan\n")

# Q3
# Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote

names = ["Alice", "Bob", "Charlie"]
for q3 in names: # loop through the names list
    q2(q3) # use function from Q2 using list of names

# Q4
# Write a function that prints the area of two passed in parameters

def q4(a,b): # expect 2 * parameters to be passed to function
    print("The area is: " + str(a * b) + "\n")
q4(252, 263) # 2 parameters separated by a comma

# Q5
# Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list

def print_list(q5_var): # function creation and pass paremeter to interemdiate var called q5_var
    for q5 in (q5_var): # Loop through q5_var and pass elements to var called q5
        print(q5) # print out q5 (each element of the list below)

q5_list = ["bob", "james", "harry"] # define list

print_list(q5_list) # call defined function and pass list 15_list to it

# Q6
# Put the following into a function:
    # If they are younger than 11, print "You're too young to go to this school"
    # If they are between 11 and 16, print "You can can come to this school"
    # If they are over 16, print "You're too old for school"
    # If they are 0, print "You're not born yet!"

def q6(age):
    if age <= 0:
        print("You're not born yet!")
    elif age < 11:
        print("You're too young to go to this school")
    elif age < 17:
        print("You can can come to this school")
    else: # If non of the above, i.e. over 16 years old
        print("You're too old for school")

q6(int(input("\nWhat is the age? ")))