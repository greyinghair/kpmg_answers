## Functions ##
# Functions are re-usable, self-contained blocks of code that do a single task such as below.

# print() # Prints to screen
# input() # Takes input from the user
# str() # Casts value to a string
# int() # Casts value to an integer
# len() # Gets the length of the string/list etc

## Fucntion create use def  (define) e.g

    # def <function_name>():
    #    <your code here>

def hello_world():
    print("\nHello big bad world!\n")

# to call the above custom function run it with (), without them it won't run:
# could call a variable within the brackets.

hello_world()

# Functions are useful to implement DRY (Don't Repeat Yourself):

### START example

def message(name):  # Define the function of hello and pass to intermediate variable
    print("Hello, " + str( name ) + "!" ) # then to change message to print, change it within the function such as "bye"

message("Alice")  # call the function message and passes "Alice" to variable called name then action of function prints
message("Bob")
message("Charlie")

print("\n") # line spacing for when running code to separate above and below result

### END Example

# You can pass multiple parameters to a function, such as name and age to put in 2 diff intermediate variable to use

### START Example

def hello(name, age):
    print("Hello, my name is " + name)
    print("I'm " + str(age) + " years old")

    age_in_10_years = age +10
    print("In 10 years i will be " + str(age_in_10_years) + " years old, crikey!\n")

hello("Dan", 40)
hello("Wendy", 38)
hello("Ai-Ren", 12)

### END Example

### Start Example

def area(x, y, z):
    print("The area is " + str(x * y * z))

area(12, 44, 6)
area(9, 11, 97)

### END Example