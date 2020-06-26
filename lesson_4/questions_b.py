# 1 .Loop through the list you created in section A and print each item out
fruit = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
for loop_fruit in fruit:
  print(loop_fruit)


# 2. Print the numbers 1 to 100 (including the number 100)
print("\n\n## Question 2 ##\n\n")
for one_to_one_hundred in range(1,101):
  print(one_to_one_hundred)


# 3. Print all odd numbers from 1 to 100
print("\n\n## Question 3 ##\n\n")

for one_to_one_hundred_odd in range(1,101,2): # increment by 2. starting at 1 to index 101 (ie. the value of 100)
  print(one_to_one_hundred_odd)

  # or
for one_to_one_hundred_odd in range(1,101):
  if one_to_one_hundred_odd % 2 == 1: # if is a remainder ie 1 = TRUE then is Odd
    print(one_to_one_hundred_odd)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip 1916, 1940, 1944, 2020)
print("\n\n## Question 4 ##\n\n")

  # Easy way
for olympic_years in range(1896, 2021, 4):
  if olympic_years != 1916 and olympic_years != 1940 and olympic_years != 1944 and olympic_years != 2020:
      print(olympic_years)

      #or better more scalable way
years_not_taken_place = [1916, 1940, 1944, 2020]
for olympic_years in range(1896, 2021, 4):
  if olympic_years in years_not_taken_place: # checks for element IN a list
    print(str(olympic_years) + " - not taken place")
  else:
    print(olympic_years)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
print("\n\n## Question 5 ##\n\n")

random = ["38", "9", "4097", "24", "1", "83", "40", "48", "33", "791"]
even = [] # Define empty list named "even"
odd = [] # Define empty list named "odd"
for random_loop in random:
    if int(random_loop) %2 == 0: # if the elements in list divisable by 2 with 0 remainder, ie Even
        even.append(random_loop) # append the number the the empty list called "even"
    else:
        odd.append(random_loop) # else (if not even, ie odd) then append the number to the empty list called "odd"
print("The number of EVEN numbers is: " + str(len(even))) # work out and print how many elements are in even list
print("The number of ODD numbers is: " + str(len(odd))) # work out and print how many elements are in odd list

  # or simpler way to just count the number of them
print("\n## Question 5 - The simpler way ##\n\n")
  # put in as an INT in list so don't use quotations for simplification
random2 = [6, 18, 12, 24, 1, 99, 16, 8, 133, 4096]
even2 = 0
odd2 = 0
for x in random2:
  if x % 2:
    odd2 = odd2 + 1
  else:
    even2 = even2 + 1
print("The number of even numbers in 2nd round is " + str(even2))
print("The number of odd numbers in 2nd round is " + str(odd2))



# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.

print("\n\n## Question 6 ##\n\n")

names = ["Dan", "Wendy", "Ai-Ren", "David", "Liz"]
for all_names in names:
    print("Hello " + all_names)



# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".  Same as for LIST but for string instead).
print("\n\n## Question 7 ##\n\n")

word = "supercalifragilisticexpialidocious"
for letter in word:
    print(letter)


# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
print("\n\n## Question 8 ##\n\n")

nums_q8 = [42, 7, 49, 3, 19]
new_list = []
for nums_squared in nums_q8:
    new_list.append(nums_squared ** 2) #list to append followed by () containing what to append with
print(new_list)

  #or if done via user input....
squared = [] # create empty list to be able to append to
for nums_q_8 in range (5): # run through the code 5 times to get 5 numbers
    number = int(input("Please pick a number..."))
    squared.append(number ** 2) # To the exponent of 2 (aka the power of 2)

# After 5 runs through print list "numbers"
print(squared)


# 9. Create a list with five names in. Write a for loop which appends Dr. to each name in the new list.
print("\n\n## Question 9 ##\n\n")

names_q9 = ["Dan", "Stacey", "Ma", "Tang", "Chorley"]
dr = []
for xy in names_q9:
    dr.append("Dr. " + xy)
dr.sort() # Sort alphabetically
print(dr) # Print dr post sort

  # or via user input including how many names to enter which will define how many times to loop
name_q9_b = []
howmany = int(input("How many names to enter?...")) # cast user input to integer
for tempnames in range(howmany):
  name_q9_b.append("Dr " + (input("What is the name?..."))) # append vlist with DR + the input from the user
print(name_q9_b)


# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz"
print("\n\n## Question 10 ##\n\n")

for xyz in range(1, 101):
    if xyz % 3 == 0 and xyz % 5 == 0:
        print("FizzBuzz")
    elif xyz % 3 == 0:
        print("Fizz")
    elif xyz % 5 == 0:
        print("Buzz")
    else:
        print(xyz)