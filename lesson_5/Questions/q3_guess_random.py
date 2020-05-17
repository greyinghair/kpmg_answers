# Rewrite Q2 so that the number being guessed is a random value from 1 to 10
import random

number = random.randint(1,10) # variable to chose random integer between 1 and 10
guess = 0 # define variable and set to zero

while number != guess: # as long as number is NOT the same as guess.  Ie input and computer values don't match..loop
    guess = int(input("Guess what number I am thinking of between 1 & 10......")) # cast input to integer
    print("You guessed " + str(guess)) # print your guess
    print("Computer generated " + str(number)) # print computer guess

# Only prints the below when loop ends as number = guess and prints both user and computer value for verification
print("Wow you guessed the same number as me " + str(number))