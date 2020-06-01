## Week 7 Questions, Section - B

# Q1
# Write a function called is_odd that will return True or False if the integer passed as a parameter is
# odd (hint: x % 2 will return true for all odd numbers)

def is_odd(q1):
    if q1 % 2: # i.e. if 1 / True, ie 1 remaining i.e. Odd
        print("Odd")
        return True
    else:
        print("Even")
        return False


q1_number = is_odd(int(input("Choose a number to work out if odd/even: ")))


# Q2
# Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'

def q2(word):
    wordbackwords = "" # Required inside function
    for q2_letter in word:
        wordbackwords = q2_letter + wordbackwords # critical the way round this goes
    print(wordbackwords)

q2("hello")


# Q3
# Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars
# on each line, E.g: **

def stars(num):
    for s in range(num):
        print("*" * (num))  # print "*" as many times as defined in num (passed from stars)
        num -= 1 # Remove value and hence number of stars by 1 on each loop

stars(int(input("How many stars?: ")))


# Q4
# Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock",
# else "Locked"

correct_code = 4321

def padlock(x):
    if x == correct_code:
        print("Unlock")
    else:
        print("Locked")

padlock(int(input("What is the passcode? ")))

# Q5
# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example,
# if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20

def q5(max):
    total_step3 = []
    total_step5 = []
    grand_total = 0
    for step3 in range(0, max+1, 3):  # Start at zero, max of input. Step of 3 & 5
        print(str(step3) + " (step-3)")
        total_step3.append(str(step3))
    for step5 in range(0, max+1, 5):
        print(str(step5) + " (step-5)")
        total_step5.append(str(step5))

    # Remove duplicates (from Step-5) (such as not having 15 in both vars)
    print("\n")
    for duplicate in total_step3: # Loop through total_step3
        if duplicate in total_step5: # If value from total_step3 matches a value in total_step5
            print("duplicate is: " + duplicate)
            total_step5.remove(duplicate) # Remove the duplicate from total_step5

    print(total_step3)
    print(total_step5)

    # Loop through both lists and + each value to grand_total as an integer
    for x in total_step3:
        grand_total += int(x)
    for y in total_step5:
        grand_total += int(y)

    print("\nSum of range is: " + str(grand_total)) # Answer should be 98 if max is 20

q5(int(input("Sum of multiples of 3 & 5 between zero and ?: ")))

# Q6
# Write a function called is_prime() that accepts a number and return True or False if the number of prime or not

def is_prime(prime):
    count = 0
    for p in range(2,(prime)): # loop from 2 through to index 1 less than the number itself, i.e. won't include the
        # number itself nor 1 but divide by everything else, if any of then can be divided by a whole number then not
        # a Prime number
        if prime % p == 0: # If the number is divisible (entirely by the number in range, then:
            print(str(prime) + " is divisible by " + str(p))
            count += 1
    if count == 0:
        print("\nPRIME" + " (count: " + str(count) + ")")
    else:
        print("\nNOT PRIME" + " (divisible by " + str(count) + " number(s) other than 1 and itself)")


is_prime(int(input("What number would you like to know whether is a prime number or not? ")))


# Q7
# Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is
# not.

def q7(word):
    backwards = "" # Create empty (str) variable
    for w in word:
        backwards = w + backwards # order is critical, if backwards + w would be forwards (this KEY line)
        print(backwards) # print the steps showing is appending backwards to w
    if backwards == word: # Compare the input both forwards and back, if match then
        print(word + " = IS a pallindrome")
    else:
        print(word + " = NOT a pallindrome")

q7(input("Word to see if pallandrome or not: "))

# Q8
# Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is
# not. Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.