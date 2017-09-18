"""
Lab 21.2        Rock Paper Scissors
--------

In this lab, you will create a Rock, Paper, Scissors game.
The user will input one of the three choices, and the computer
will pick one at random. The winner will be determined by the
rules of Rock, Paper, Scissors that you play in the real world.

"""

from RockPaperScissors import *

def main():
    response = "Y"
    """
    while response is "Y" or "y"
        user input "Rock-Paper-Scissors - pick your weapon[R,P,S]:: "
        rps = new RockPaperScissors object - user input is parameter
        print rps
        print the output of determineWinner() on rps

        response = user input: "Do you want to play again?"
    """
    while response == "Y" or response == "y":
         rps = RockPaperScissors(input("Rock-Paper-Scissors - pick your weapon[R,P,S]:: "))
         print(rps)
         print(rps.determineWinner())

         response = (input("Do you want to play again? "))
         if response == "Yes" or response == "yes" or response == "YES":
             main()

main()
