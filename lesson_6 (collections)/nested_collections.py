## You can nest collections inside collections. Such as...

# A list containing multiple other lists.  aka List-of-Lists
phone_grid = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]

for row in phone_grid: # puts first list of list in "row" variable on 1st loop, then loop for each other list of list
    for column in row: # loops and pulls each element from the 1st list of list and prints out each element
        print(column)


# a List of Dictionaries
contacts = [
    {"firstname": "Dan", "lastname": "Stacey"},
    {"firstname": "Wendy", "lastname": "Stacey", "Phone": "+441726666666"},
    {"firstname": "Charlie", "lastname": "Tango"}
]

for person in contacts: # loop through and extract each dictionary
    if "Phone" in person: # look for presence of key named "Phone" (case sensitive) and if found:
        print(person["firstname"]) # print value of key "firstname" # Wendy

## Next example
# Adding names to a dictionary within a list with user input
namelist = []
firstname = None # must be uppercase "N" for this value to be none

while firstname != "": # loop as long as variable firstname has no value, ie when you enter blank value stop looping
    firstname = input("What is your firstname?: ")
    surname = input("What is your surname?: ")

    if firstname and surname: # only True (i.e. run) if both variables have a value.  aka validation.
        namelist.append({"1stname": firstname, "2ndname": surname}) # append to list with new dictionary on each loop

print(namelist) # Print list