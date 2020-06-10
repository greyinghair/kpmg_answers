import time # import the time module

start_time = time.time()


## insert code to run here ##

count = 0
while count < 1000000: # Loop 1M times
    count += 1 # Increment count by 1
    print("I am on loop number.." + str(count)) # Print what loop number I am on

## End code run ##

end_time = time.time()
print("Your code completed in " + str(end_time - start_time) + " seconds")