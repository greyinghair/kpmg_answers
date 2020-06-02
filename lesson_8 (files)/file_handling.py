## Files handling
# As already learned in "file_open.py" USING READ MODE

#   f = open("<filename", "<mode>")
# e.g.:
#   f = open("my_file.txt","r") # means open file named my_file.txt and open in Read mode ("r" = read).

# Full options of values to use as parameter without the open function.


# Action READ "r" - opens a file for reading, error if the file does not exist
word = open("z_read.txt","r") # Read, error if file doesn't exist

# Action APPEND "a" - opens file for appending, creates the file it if doesn't exist
word = open("z_append.txt","a") # Append, create file is doesn't exist

# Action WRITE "w" - opens file for writing, create the file if it doesn't exist
word = open("z_write.txt","w") # Write, create file if it doesn't exist. Will overwrite existing file.

# Action CREATE "x" - creates the specified file, returns error if file exists
word = open("z_create.txt","x") # Create file, error if already exists