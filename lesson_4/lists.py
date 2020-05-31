## Lists are strings captured in [] separated by commas
# e.g.
names = ["Alice", "Bob", "Charlie"]
# Print using indexing which represents each element starting at zero
print(names[0]) # Alice
print(names[1]) # Bob
print(names[2]) # Charlie


## To ADD to an existing list with 
#
#   <variable/list>.append
#
# e.g. add "Dave" to above 'names' variable
names.append("Dave")
print(names) # ['Alice, 'Bob', 'Charlie', 'Dave']

## To INSERT at specific Index in  list
#
# <list>.<insert>[<index#>, <value]
names.insert(0, "Jimbo")
print(names) # ['Jimbo', 'Alice', 'Bob', 'Charlie', 'Dave']

## To REPLACE existing element, define the list with the index position to replace
# along with the new value.
# e.g. to replace Charlie (which is index position 2) with Chris:
names[2] = "Chris"
print(names) # ['Jimbo', 'Alice', 'Chris', 'Charlie', 'Dave']


## To DELETE an element in a list, define variable with DEL and the index position 
# e.g. to delete 'Bob' (which is index position 1 (2nd from the left)):
del(names[1])
print(names) # ['Jimbo', 'Chris', 'Charlie', 'Dave']

## To Remove/Delete an element based on value:
steps = [2, 5, 10]
steps.remove(5)
print(steps) # [2, 10]

## To check presence of an element within a list use IN within the statement
# e.g. to see if "Eve" is in the list
names = ["Alice", "Bob", "Charlie"]
if "Eve" in names:
  print("Eve is here")
else:
  print("Eve is NOT here")


## To see the LENGTH of a list, ie the number of items in a list use the LEN statement
print(len(names)) # 3 items in the list


## SORT list 
#
#   alphabetically <list>.sort()
#
# e.g.
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names) # Should be ['Alice', 'Bob', 'Charlie']