"""==================================================
* Ex_03: Dice Roll
* Create a game that simulates rolling dice
* against the computer and prints the winner.
=================================================="""


import random

def diceRoll(yR, cR):
    """Conditional logic:
    if your roll was better than the computer's
        set winner to you"""

    """if the computer's roll was better"""
    """set winner to Computer"""

    if yR > cR:
        winner = "You"
    if yR < cR:
        winner = "Computer"
    if yR == cR:
        winner = "It's a tie!"

    return winner

def main():
    yourRoll = random.randint(1, 7)
    compRoll = random.randint(1, 7)

    winner = diceRoll(yourRoll, compRoll)

    print("You rolled...........", yourRoll)
    print("Computer rolled......", compRoll)
    print("And the winner is....", winner)
main()
