## Packing & Unpacking
# * and ** are packing and unpacking examples

# example (of single * for arg)

numbers = [1, 3, 5, 7]
more_numbers = [*numbers, 9, 11, 13] # * symbol to unpack numbers list into this 2nd list
print(more_numbers)

## use star character in places other than functions

## Can do the same within dictionary for double * (**)

# example (of ** / dictionary)

fruit_stock = {"apples": 15, "oranges": 20, "carrots": 10} # such as stock from previous day
latest_stock = {**fruit_stock, "apples": 10} # takes fruit_stock but then overwrite "apples" value from 15 to 10

# above is useful as dictionary cannot have duplicate key names, so append one dict to another and change a value,
# if same key already in destination dictionary then that one is kept and the source key/value is discarded.

print(latest_stock) # apples changed from 15 in stick to 10.  orange & carrots remain unchanged

# example 2 (of **)

fruit_stock = {"apples": 15, "oranges": 20, "carrots": 10}
delivery = {"mangos": 12, "bananas": 18}
latest_stock = {**fruit_stock, "apples": 21, ** delivery} # Define apples vale so apples from fruit_stock discarded.
# appended delivery dict to latest_stock

print(latest_stock) # {'apples': 21, 'oranges': 20, 'carrots': 10, 'mangos': 12, 'bananas': 18}

# example 3 (of **)

def area(x, y ,z): # function expects 3 parameters to be passed
    return x * y * z # when function called return output of calculation

# list containing dictionaries, can scale to as many dicts as you wish, e.g. as many as you need to import from a file
data = [
    {"x": 3, "y": 12, "z": 42}, # have to be separate dicts as same keys in each dictionary
    {"x": 13, "y": 9, "z": 11},
    {"x": 183, "y": 3, "z": 42}
]

for dicts in data: # loop through each dict in the list called 'data'
    print(area(**dicts)) # use ** for wildcard dictionary to pass each dict to the function and then print what's
    # returned.  keeps the code scaleable by just adding new dicts to the data list either manually or import from files

# exmaple 4 (of ** with function)

def add_contact(**kwargs):
    for key, value in kwargs.items(): # Takes both keys and value and passes to variables. .items() returns
        # keys/values from a dictionary
        print(key + " : " + value)

contact = {"forename": "Daniel", "Surname": "Stacey","carrots": "5"}

add_contact(**contact) # takes dict, extracts key & values and prints to screen