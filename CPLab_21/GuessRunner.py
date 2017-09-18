"""
Lab 21.1        Guessing Game
---------
In this lab, you will write a program that plays a guessing
game with you. The program picks a random number between 1 and
a number of your choosing. When you guess right the program will
tell you how many guesses it took to get the right answer.
"""

from GuessingGame import *
response = "Y"

"""
while response is "Y" or "Y"....
    nums = input for "How many numbers"
    game is a new GuessingGame object with [nums] in the parameters.
    run playGame()
    set response to input: do you want to play again?
"""
while response == "Y" or response == "y":
    game = GuessingGame (int(input("Guessing Game - how many numbers?")))
    print(game.playGame()
          )

    response = input("Do you want to play again?")
