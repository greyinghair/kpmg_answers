# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list
fruit = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(fruit)


# 2. Add "Grapes" to the list and print the list
fruit.append("Grapes")
print(fruit)


# 3. Change "Pears" to "Strawberries" and print the list
fruit[2] = "Strawberries"
print(fruit)


# 4. Remove "Apples" from the list and print the list
del(fruit[0])
print(fruit)

# 5. Print out the current length of the list
print(len(fruit))

# 6. Order the list alphabetically
fruit.sort()

# 7. Print out the list again
print(fruit)