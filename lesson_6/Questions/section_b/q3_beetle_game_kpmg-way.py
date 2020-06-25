# Q3
# The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
# If you roll a 6, you can draw the body
# If you roll a 5, you can draw the head
# If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
# If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
# If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
# If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
# You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
# The player to complete the beetle in the fewest rolls of the dice wins.
# i. Create the beetle game.

import random

parts_list = {
     "1": "mouth",
     "2": "eye",
     "3": "antennae",
     "4": "legs",
     "5": "head",
     "6": "body"
}

beetles = [] # list so can draw multiple players at same time
loopcount = [] # to store results of how many rolls of dice for each player in a single list

## Number of players.....
players = None # create variable with No value so can be used in loop below for user validation
players_allowed = range(1,100)# Value from 1 -> 100
while players not in players_allowed: # keep asking for number of players until is in range above
    players = int(input("How many players? (1-99) "))
## End number of players

for x in range(players): # Loop as many times as there are players
    # Append to beetles list the number of items still required of each item on each run through, value as Integer
    # before play starts
    beetles.append({
        "1": 1, # mouth
        "2": 2, # eyes
        "3": 2, # antennae
        "4": 6, # legs
        "5": 1, # head
        "6": 1 # body

    })
    loopcount.append(0) # Set score to in a list, zero for each player, all in same list. 1 element per player.

#print(beetles) # uncomment this line for debugging
#print(scores) # uncomment this line for debugging

print("start of game....")
winner = None

while winner is None: # Loop until is a winner

    for current_player in range(players): # loop for as many players as there are
        player_roll =  input( "\nPlayer number: " + str(current_player + 1) + ", press enter to roll")
        dice = random.randint(1, 6)  # Generate random number between 1 & 6
        loopcount[current_player] +=1 # Add loopcount to index value based on player number to keep score per player
        # in a single list, this is a key part
        print("You rolled a " + str(dice) + " (" + parts_list[str(dice)] + ")")

        if dice > 0:
            # Invalid spin statements
            if dice == 6 and beetles[current_player]["6"] == 0: # If you roll 6 and body 0, ie non needed
                print("You already have a body")
            elif dice == 5 and beetles[current_player]["5"] == 0: # if you roll 5 for head and num of heads needed is 0
                print("You already have a head")
            elif dice == 4 and beetles[current_player]["6"] == 1: # If num of bodys required still 1
                print("You can't have legs without a body")
            elif dice == 3 and beetles[current_player]["5"] == 1: # If num of heads required still 1
                print("You can't have antennae without a head")
            elif dice == 2 and beetles[current_player]["5"] == 1:
                print("You can't have eyes without a head")
            elif dice == 1 and beetles[current_player]["5"] == 1:
                print("You can't have a mouth without a head")
            # Start of valid rolls to remove what is still left to get
            else:
                print("You got a " + parts_list[str(dice)]) # Pull from list based on number rolled what the user got
                if beetles[current_player][str(dice)] > 0: # without this could have negative values for items
                    beetles[current_player][str(dice)] -= 1 # Remove 1 from number in list for user of what parts remain
                    #print(beetles[current_player]) # uncomment this line for debugging whats left to collect
            for list in beetles[current_player]: # loop through dict for current player for remaining parts
                if beetles[current_player][list]: # If value is True, i.e. NOT 0. i.e. still parts left to get
                    print("You need " + str(beetles[current_player][list]) + " " + parts_list[str(list)])

            # Has user won on this spin (got zero parts left to get from beetles list) ?
            if sum(beetles[current_player].values()) == 0:
                winner = current_player

print("The winner is player: " + str(winner + 1)) # Winner (correcting index vs player number)

print("\nThe overall scores were..." + str(loopcount))