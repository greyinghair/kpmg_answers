## File - write

# Create the file and write "Hello world"
f = open("./tmp/example.txt", "w") # Create file example.txt in /tmp
f.write("Hello world") # Write "Hello world" to file, anything inside () will be passed to file
f.close() # Not a requirement but best practice to close file after writing to it

# Append "it's nice to be here" to the file created above, append is normally what you would use
f = open("./tmp/example.txt","a") # a for append
f.write("It's nice to be here")
f.close()

# Print contents of file (has to open again)
f = open("./tmp/example.txt","r") # Just need to read ("r"), not right
print(f.read())
f.close()