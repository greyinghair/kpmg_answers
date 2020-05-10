# You can stop a loop with the 'break' command, the below example shows this even if user says loop for 100 times
# It is useful to put after a loop statement to limit the max number of loops

num_of_loops = int(input("How many time should I loop? "))
for x in range(num_of_loops):
    print("Hello")
    # x starts at 0, so to break after 5 loops we do this
    if x >= 4:
        break

# It is useful to put after a while loop statement to stop an infinite loop such as below
count = 0
while True:
    print("I am on loop number.." + str(count))  # Print what loop number I am on
    count += 1  # Increment count by 1
    if count >= 1000000:
        print("I have looped 1M times which is a lot, time to BREAK")
        break