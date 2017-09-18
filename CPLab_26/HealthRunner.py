"""
=============================
Import all from GameHealth
Import random
=============================
"""

from GameHealth import *
import random

player = GameHealth()
print(player)
turn = ""
damage = 0
amount = 0

while turn != "q" and player.getHealthCount() > 0:
    turn = input("Your turn! Enter when ready: ")
    damage = random.randint(1, 3)
    amount = random.randint(1,7)
    print(player.takeDamage(damage, amount))
    print(player)

print("You died")
"""
=============================================================
new GameHealth object called player
print player
new variable turn: set to an empty String
new variable damage: set to 0
new variable amount: set to 0

while loop: run as long as turn is not equal to "Q"
and healthCount is greater than 0...
    set turn to user input: "Your turn! Enter when ready: "
    set damage to random number between 1 and 2
    set amount to random number between 1 and 6
    print takeDamage() output with params damage and amount
    print player object

print "You died!!!" as the loop exits
=============================================================
"""


