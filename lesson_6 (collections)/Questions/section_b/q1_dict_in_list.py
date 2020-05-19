# Q1
# 1 - Ask the user to enter a persons name, if they enter a name, ask for the persons age.
# 2 - Store this information in a dictionary inside a list.
# 3 - Continue to ask for names until no name is given.
# 4 - Then print out all of the names and ages collected.

userdata = []
name = None
age = None

while name != "":
    name = input("Enter a name: ")
    if name:
        age = int(input("What is their age?: ")) # Age being an integer should be cast as such.  Default input is string
        userdata.append({"name": name, "age": age}) # create dictionary and append to userdata list on each loop

# print(userdata)

print("Name\tAge") #Print with tab in between for formatting like headings of a table
for contact in userdata: # Will loop for the same number of times as there are elements (dictionaries) in the variable
    print(contact["name"] + "\t" + str(contact["age"])) # Include tab in quotes for spacing formatting

