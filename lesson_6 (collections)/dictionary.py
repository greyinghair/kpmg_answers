# Dictionary uses similar syntax as a SET {}
# KEYS MUST be UNIQUELY named
# Dictionaries aren't ordered/sorted
# Dictionaries contain keys with their associated values e.g.

my_dict = {
    "key" : "value",
    "key2": "value2"
}

print(my_dict)

# A KEY can online contain a SINGLE VALUE, couldn't have "small", "medium", but could have "s/m".
# Next example of use of Dictionary:
shirt = {
    "size": "medium",
    "colour": "red"
}

student = {
    "name": "John Jonker",
    "year": 12,
    "form_tutor": "Miss Dripalot"
}

# Reference a key in the same way as you reference a list with index

    #   (dict_name["key_name"])

print(shirt["colour"]) # Red
print(student["year"]) # 12

# Add a new key/value to a dictionary (i.e. APPEND):

    #   dict_name["additional_key_name"] = "new_value"

shirt["material"] = "cotton"

print(shirt["material"])

# Change value of existing key is the same as adding a new key/value pair as above
# As in a list referencing Index within [] in a dictionary you reference the key name inside the []
# e.g. change shirt size to large:

shirt["size"] = "large"
print("New shirt size is " + (shirt["size"]))

# To delete the key/value, sme as in lists, but reference the key name to delete which also removes the value:
print(shirt) # before deletionof colour key and associated value
del(shirt["colour"])
print(shirt) # after deletion of colour

# Check for Key within a dictionary. (doesn't check for a value, ONLY a key name)
if "material" in shirt:
    print("Shirt is made of " + shirt["material"])

# Loop example with Dictionary
shirt = {
    "colour": "Green",
    "material": "cotton"
}

for x in shirt: # loop for each key, of which are 2.
    print(x + " = " + (shirt[x])) # print the key within dictionary as well as the value of said key