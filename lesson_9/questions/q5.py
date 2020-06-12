# Q5
# Modify your previous answer to save key/value pairs in a file:
# fname: Alice
# lname: Smith
# phone: 555-1234

def tofile(**kwargs):
    file = open( "files/question5.txt", "a" )
    for key, value in kwargs.items(): # have you use .items() for this to work, passes key and value to those

        # option-1 (concatenation)
        # file.write(key + ": " + value + "\n")

        # option-2 (using a formatted string) instead of concatenation
        file.write(f"{key}: {value}\n")
        print(f"{key}: {value}")

    file.close()

data = {"fname": "Alice", "lname": "Smith", "phone": "555-1234"}

tofile(**data)