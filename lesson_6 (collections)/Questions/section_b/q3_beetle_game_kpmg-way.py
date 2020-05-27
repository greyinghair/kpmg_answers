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

parts = {
    "1": "mouth",
    "2": "eye",
    "3": "antennae",
    "4": "leg",
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
        print(dice)
        loopcount[current_player] +=1 # Add loopcount to index value based on player number to keep score per player
        # in a single list, this is a key part
        if dice == 6 and not beetles({"6"}): # If you roll 6 and body NOT set to True, ie no body
            print("You can draw a body")
            beetles([current_player{"6":}]) -= 1
            print(beetles[current_player])

print("The winner is " + str(winner)) # Winner

print("\nThe overall score were..." + str(loopcount))


# win = {
#     "body": True,
#     "legs": 6,
#     "head": True,
#     "antenna": 2,
#     "eyes": 2,
#     "mouth": True
# }
#
# overall = []