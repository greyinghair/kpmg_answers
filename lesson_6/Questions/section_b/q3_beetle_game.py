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
players = int(input("How many players? (1-3) ")) # Set
playernumber = 0 # Incremented after each players go to identify player #

# Match the below to win
win = {
    "body": True,
    "legs": 6,
    "head": True,
    "antenna": 2,
    "eyes": 2,
    "mouth": True
}

overall = []

for x in range(players): # Loop for number of players that there are

    loopcount = 0  # Incremented after each roll within sub loop
    # Starting off with nothing (has to go inside loop or values don't reset for each player and never makes 2nd loop)
    results = {
        "body": False,
        "legs": 0,
        "head": False,
        "antenna": 0,
        "eyes": 0,
        "mouth": False
    }

    while results != win: # within each loop, loop again until get same results as for a win per player

        print("\nPlayer number: " + str(x + 1))  # Print player number (index +1)
        loopcount +=1 # Increment loopcount once per loop
        print("Roll number: " + str(loopcount)) # uncomment line for troubleshooting
        roll = random.randint(1, 6)  # Generate random number between 1 & 6
        print("\nYou rolled a " + str(roll))
        if roll == 6 and not results.get("body"): # If you roll 6 and body NOT set to True, ie no body
            print("You can draw a body")
            results["body"] = True # Change body boolean to True
        elif roll == 6 and results.get("body"): # If you already have a body (True) and roll 6
            print("You already have a body")
        elif roll == 5 and not results.get("head"): # If body is True ie you already have a body and you roll a 5
            print("You can draw a head")
            results["head"] = True # Change head boolean to True
        elif roll == 5 and results.get("head"): # If you roll 5 and already have a head
            print("You already have a head")
        elif roll == 4 and results.get("body") and not results.get("legs") == 6: # If you roll 4 and already have a body
            print("You can draw a leg")
            results["legs"] += 1
        elif roll == 4 and results.get("body"): # 4, and body but already have 6 legs
            print("You already have 6 legs")
        elif roll == 4: # 4, no body
            print("You need a body before legs")
        elif roll == 3 and results.get("head") and not results.get("antenna") == 2:  #If roll 3, have head and not 2 ant
            print("You can draw an antenna")
            results["antenna"] += 1
        elif roll == 3 and results.get("head"):  # roll 3, and body but antenna is 2
            print("You already have 2 antenna")
        elif roll == 3:  # 3, no head
            print("You need a head before antenna")
        elif roll == 2 and results.get("head") and not results.get("eyes") == 2:  # If roll 2, have head and not 2 eyes
            print("You can draw an eye")
            results["eyes"] += 1
        elif roll == 2 and results.get("head"):  # roll 2, and body but already have 2 eyes
            print("You already have 2 eyes")
        elif roll == 2:  # 2, no head
            print("You need a head before eyes")
        elif roll == 1 and results.get("head") and not results.get("mouth"): # If roll 1, have head but no mouth
            print("You can draw a mouth")
            results["mouth"] = True # Change mouth value to true
        elif roll == 1 and results.get("head"):  # roll 2, and body but already have 2 eyes
            print("You already have a mouth")
        elif roll == 1:  # 2, no head
            print("You need a head before a mouth")

        print(input("\n\tPress enter when ready for next roll")) #comment out to loop through rolls without pause/input
        # end of a single roll

    # After player loops through and completes beetle....
    # increment at end of each players loop. player 1 after 1 loop, player 2 on 2nd loop etc.
    playernumber += 1

    # Record number of rolls per player, append new dict to list
    overall.append([{
        "Player": playernumber,
        "Score": loopcount
    }])

    print("Congrats player-" + str(playernumber) + ", you have a full beetle your turn is over\n\n")
    # End of player number x's go

# print overall results shows player x vs number of rolls of dice and declare the winner
print("Player\tNum of rolls (lowest wins)")
print("######\t############\n")
for a in overall: # loop as many times are there were players (i.e. 1 per dictionary)
    for b in a: # for score in y: # loop through each element in each dictionary
        print(str(b["Player"]) + "\t\t" + str(b["Score"]))

print("\n")
print(overall)