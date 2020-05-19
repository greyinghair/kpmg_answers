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
rand = random.randint(1,6)
players = int(input("How many players? (1-3) "))
win = [{
    "body": True,
    "legs": 6,
    "head": True,
    "antenna": 2,
    "eyes": 2,
    "mouth": True
}]

results = []

print(win)

# how many players
# while loop
#     if dice == 6:
#         print("Draw body")
#         player(#).append([{"throw(x)": )}]
#     while someone not won