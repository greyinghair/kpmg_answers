# Create a rock, paper, scissors game which is run against computer.
# This is a game where you select either rock/paper/scissors and you compare it to your opponents choice.
# Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again
# Expand this so that its best of 3 games

import random
rps = ["rock", "paper", "scissors"] # options for random module to use for computer guess
user_guess = []
computer_guess = []
user_win = 0 # number of times user wins
computer_win = 0 # number of times computer wins

while user_win < 2 and computer_win < 2:
    user_guess = input("Rock, Paper or Scissors? :").lower() # take input from user guess and make lower case
    if user_guess not in rps : # Sanity check if user input is not in the rps list
        print("Invalid move")
    computer_guess = random.choice(rps) # random choice from "rps" list
    print("\nComputer: " + (computer_guess))

    # Logic for calculating who wins what
    if user_guess == "rock" and computer_guess == "scissors" or user_guess == "paper" and computer_guess == "rock" or\
            user_guess == "scissors" and computer_guess == "paper":
        user_win += 1
        print("\nPoint to you\n")
    elif user_guess == "scissors" and computer_guess == "rock" or user_guess == "rock" and computer_guess == \
            "paper" or\
            user_guess == "paper" and computer_guess == "scissors":
        computer_win += 1
        print("\nPoint goes to computer\n")
    elif user_guess == computer_guess:
        print("\nDraw\n")


print("# of user wins = " + str(user_win))
print("# of computer wins = " + str(computer_win))

if user_win >= 2:
    print("\nYou Win!")
else:
    print("\nYou Lose!")