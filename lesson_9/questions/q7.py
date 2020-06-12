# Q7
# Google the Python CSV library, and modify question 5 to save the data as a csv file.
# Make it so that you can enter as many contacts as you want and they each end up on a new row within the csv.

import csv

def tofile(**kwargs):
    with open( "files/question7.csv", "a") as file:
        writer = csv.DictWriter(file, kwargs.keys())
        writer.writeheader() # use this line to create header which is the keys in each column
        writer.writerow(kwargs)


tofile(fname = "Dan", lname = "Stacey", dob = "040280")