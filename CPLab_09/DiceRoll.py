"""==================================================
* Ex_03: Dice Roll
* Create a game that simulates rolling dice
* against the computer and prints the winner.
=================================================="""
import random

def diceRoll(yR, cR):
    if yR > cR:
        winner = "You"
    if cR > yR:
        winner = "Computer"

    winner = winner

    return winner

def main():
    """Takes random numbers and uses as input."""
    yourRoll = random.randint(1, 7)
    compRoll = random.randint(1, 7)

    winner = diceRoll(yourRoll, compRoll)

    print("You rolled...........", yourRoll)
    print("Computer rolled......", compRoll)
    print("And the winner is....", winner)

main()
