# Q5
# Modify your previous answer to save key/value pairs in a file:
# fname: Alice
# lname: Smith
# phone: 555-1234

def tofile(**kwargs):
    file = open( "files/question5.txt", "a" )
    for key, value in kwargs.items(): # have yo use .items() for this to work, passes key and value to those
        # variable names
        file.write(key + ": " + value + "\n")
    file.close()

data = {"fname": "Alice", "lname": "Smith", "phone": "555-1234"}

tofile(**data)