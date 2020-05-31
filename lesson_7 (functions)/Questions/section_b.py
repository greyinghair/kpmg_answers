## Week 7 Questions, Section - B

# Q1
# Write a function called is_odd that will return True or False if the integer passed as a parameter is
# odd (hint: x % 2 will return true for all odd numbers)

def is_odd(q1):
    if q1 % 2: # i.e. if 1 / True, ie 1 remaining i.e. Odd
        return True
    else:
        return False

q1_number = is_odd(int(input("Choose a number to work out if odd/even: ")))


# Q2
# Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'

wordbackwords = []

def q2(word):
    recompiled = None
    for q2_letter in word:
        wordbackwords.insert(0, q2_letter) # Insert list Method at Index 0
    print(wordbackwords)

q2(input("What is your word? "))


# Q3
# Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars
# on each line, E.g: **

# def stars(num):
#     loopcount = 0 # define a variable within function
#     for s in range(num):
#         if loopcount < 0:
#             print("*")
#         else:
#             for y in s:
#                 print("*")
#                 loopcount += 1
#
# stars(3)

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

# Q8
# Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is
# not. Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.