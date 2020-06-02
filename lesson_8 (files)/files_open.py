## Files - opening files:

#   f = open("<filename", "<mode>")
# e.g.:
#   f = open("my_file.txt","r") # means open file named my_file.txt and open in Read mode ("r" = read).

f = open("names_file.txt","r") # open file but name, read and store in variable named f
print(f.read()) # print variable f with mode of read, won't work with just print(f)


# Using for loop to cycle through elements in file. Prints \n from the file in python so each line from file uses 2
# lines in python
names = open("names_file.txt","r")
for x in names:
    print(x) # is print but could be anything, calculation, function etc


# Pull numbers from a file and add together:
num_file = open("numbers_file.txt","r")
total = 0
for nums in num_file: # Loop through the file
    total += int(nums) # Add eah element to var outside the loop.  Cast var str to an int.
print(total)