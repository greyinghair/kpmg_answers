# Q1
# Create a function that returns the first and last letters of the word passed in as separate variables.

def first_last(*args):
    for x in args: # loop each word
        for y in x: # loop each letter in word
            return (y[0],y[-1]) # print index 0 and index -1 (ie 1st & last)


# List to add as many strings to as required
words = ["daniel", "stacey"] # d l, s y

# Call function and pass the list 'words'
first_last(words)