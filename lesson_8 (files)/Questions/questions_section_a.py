# Section A
# 1.Read the file 'jabberwocky.txt' and print its content to the screen
file = open("jabberwocky.txt","r")
print(file.read())

# 2.Read the file 'austen.txt' and print the amount of lines in the file
count = 0
austen = open("austen.txt","r")
for x in austen:
    count +=1
print("\n" + str(count) + " lines\n")

# 3.Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file
num = open("numbers.txt","r")
total = 0
for y in num:
    total += int(y) # cast to int otherwise is a string trying to add to an integer
print(total)