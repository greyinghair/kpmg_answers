## Enumerate, loops through a list of items and creates a counter.
# use it in the same way as range within a loop, reference a variable/file
# for it to extract data but also to count such as below example
#
# instead of "for x in blah".  it is...
#
#       for x, y in enumerate(blah) # where x is count and y is data from blah

file = open("names.txt", "r")
namedict = {}
for count, data in enumerate(file): # count is the numerical count for loop and data is data from parameter ()
        # remove the trailing newline to remove whitespace wich <var>.replace("replace", "with">)
        print("Line " + str(count) + ": " + data.replace("\n", ""))
file.close()