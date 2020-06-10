count = 0
while 1 + 1 == 2: # 1+1=2 will always be true, hence loops runs forever
    count += 1 # Increment count by 1
    print("I am on loop number.." + str(count)) # Print what loop number I am on
    if count >= 9999999: # after 9.999M loops
        break # Stop
