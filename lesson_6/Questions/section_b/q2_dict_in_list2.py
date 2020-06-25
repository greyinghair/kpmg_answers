# Q2
# Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. Each item in the menu
# should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly
# dish).
# 1 - Print out the entire menu.
# 2 - Print out the name of the vegetarian option(s).

menu = [] # define list
dish_input = None
count = 0 # set loop count to zero
yes_or_no = ["y", "n"] # List of acceptable strings for answer to question in loop
number_of_dishes = int(input("How many dishes? ")) # User to decide how many dishes to enter

while count != number_of_dishes: # loop as many times as defined in number_of_dishes
    dish_input = input("What is the name of the dish? ")
    veggie = None # define as non within loop
    if dish_input: # if dish is not null value then run below code (input validation)
        count += 1  # Increment count 1 per loop
        price = float(input("How much is the dish? "))
        while veggie not in yes_or_no: # has to be "y" or "n" as per variable.
           veggie = input("Is vegetarian? (y|n)? ")
        if veggie == "y":
            menu.append( [{"dish": dish_input, "cost": price, "is_veg": True}] )
        else:
            menu.append([{"dish": dish_input, "cost": price, "is_veg": False}])


## print entire menu
print("\nFullmenu")
print("\tDish\tPrice") # Create output heading

for fullmenu in menu: # Loop through each dictionary (one per item)
    for x in fullmenu: # Loop through each element within the dictionary
        print("\t" + x["dish"] + "\t £" + str(x["cost"])) # print value of dish and value of cost with tab inbetween

print("\n\n")

## print vegetarian options only

print("Vegetarian Menu")
print("\tDish\tPrice") # Create output heading

for x in menu: # Loop through each dictionary (one per item)
    for vegetarian in x: # Loop through each element within the dictionary
        if vegetarian["is_veg"]: # If is_veg is true then:
            print("\t" + vegetarian["dish"] + "\t £" + str(vegetarian["cost"])) # print value of dish and value of cost with tab