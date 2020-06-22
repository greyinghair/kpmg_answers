# Q7
# Google the Python CSV library, and modify question 5 to save the data as a csv file.
# Make it so that you can enter as many contacts as you want and they each end up on a new row within the csv.

import csv

def tofile(writer, **kwargs): # writer variable triggers open of csv file in write mode
    # and writes headers and user input
    writer.writerow(kwargs.values()) # only write values, assumes keys are same

fields = ["fname", "lname", "dob"] # to add to top of CSV columns

file = open( "files/question7.csv", "a")
writer = csv.writer(file)

# Add in field header
writer.writerow(fields)

# Get user input and loop through fields list as values asking user for keys and store in dict
name = True
while name:
    userinput = {}
    for x in fields: # loops as many times as are fields
        userinput[x] = input(x + ": ").lower() # ask user for input for field (loop / index no) and make lowercase
        if userinput[x] == "": # when empty values, ie enter key hit
            name = False # change name to false and hence stop input loop
    #print(userinput) # uncomment start of line for debugging

    # At end of loop call function
    tofile(writer = writer, **userinput)

file.close() # close file at end of loop