###########
## LOOPS ##
###########

# for <new variable> in <name of LIST to run loop through>:
#   # Runs once for each element in items
#   <code>

# FOR Loops will iterate through elements.
# in the below example we use FOR to loop through the elements
# IN the list (names) and pipe each result to another variable
# called person and then print (person).  Each loop will overwrite
# the value of (person) with the next element.  So will print each
# element in the list before starting over and repeating the process
# for the next element in the list.
name =["Alice", "Bob", "Charlie"]

for person in name:
  print(person)

  # Alice
  # Bob
  # Charlie

# The variable of (person) hold the last element as queried from the list of (name)
print(person) # Charlie

## Loop Ranges ##
#
# To run a loop for a fixed number of times, in this example will be 5 times (as python runs from zero that will be 0 -> 4)
for my_number in range(5):
  print(my_number)
  # 0
  # 1
  # 2
  # 3
  # 4

# Run from x - > y.  X being thr starting number and y being the index.
# so the below starts at 50 upto the index of 60 (which is 59 as python starts at 0)
for my_number in range(50,60):
  print(my_number)

# Below example shows range(x, y ,z)
# where x = starting number.  y = end index.  z = increment between start/end.
# example, loop start = 2000.  loop end = 2100.  increment = 5
for my_number in range(2000,2100,5):
  print(my_number)