# To print the time it takes from start of code to end
# Put current ime into variable pre start of code then
# Put time into another variable at the end and then
# subtract begining time from end time as below.

import time # import the time module

start_time = time.time()


print("poo poo")
  ## insert code to run here ##


end_time = time.time()
print("Your code completed in " + str(end_time - start_time) + " seconds")