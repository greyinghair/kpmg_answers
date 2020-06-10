# Q7
# Google the Python CSV library, and modify question 5 to save the data as a csv file.
# Make it so that you can enter as many contacts as you want and they each end up on a new row within the csv.

import csv

def tofile(**kwargs):
    with open( "files/question7.csv", "a" ) as file:
        for key, value in kwargs.items(): # have yo use .items() for this to work, passes key and value to those
            csv.writer(file, key + ":" + value)

data = {"fname": "Alice", "lname": "Smith", "phone": "555-1234"}

tofile(**data)