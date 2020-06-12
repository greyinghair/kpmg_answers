# Q3
# Create a function that takes a file name and word. Search the file to find all lines that start
# with the given word.
#
# Test your function using the file 'austen.txt' and find all lines that begin with "Mr".
# Hint: is a function that returns True/False if a string ends with a value...
#   maybe there is one that checks to see if a string "starts with"?

# should be 4.  1 of the lines starts "Mr. instead of Mr. so need to detect remove the starting "

filename = open("files/austen.txt","r")
word_to_find = "Mr"

def find(word, file):
    count = 0
    ignore = ["\""] # Have to escape the quotation "
    for x in ignore: # loop for each entry in ignore list
        for n, line in enumerate(file): # loop for each line in the file and also pass loop/i.e. line to var n
            if line.startswith(word) or line.startswith(x + word): # line stars with word or ignore var followed by word
                print("Line: " + str(n + 1), line) # show the line found to match on each loop. +1 as index starts as 0
                count += 1 # Increment count on each detection

    file.close()

    return count # return value of count post loop

print(find(word_to_find,filename))