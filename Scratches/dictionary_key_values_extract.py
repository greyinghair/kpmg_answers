## Option 1 (using loop)

stuff = {"forename": "Dan", "surname": "Stacey", "D.O.B": "04/02/80"}

for x in stuff:
    print(x + " : " + stuff[x]) # x = key.   variable[x] = value at index position relative to loop


## Option 2 (using items())

stock = {"carrots": 6, "egg": 24, "bread": 12}

for key, value in stock.items(): # .items() extracts key/value pairs respectively into proceeding variable names
    print(key + " : " + str(value)) # cast value variable to str as are int in dict and cannot contatonate