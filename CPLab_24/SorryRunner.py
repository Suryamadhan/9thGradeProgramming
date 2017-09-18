"""
================================================================
Lab_24.2            Sorry Game
---------
In this lab, you will be writing a program that emulates
the classic came "Sorry". You will move 5 pieces around
a track that is 18 spaces long against a second player. The
program simulates a dice roll to move pieces. If a player
lands on a spot where your piece is, your piece will be moved
back to square 0. The player that completes 5 laps first wins.
================================================================
"""

from Sorry import *
s = Sorry()
print(s)
while s.play():
    print(s)

print("\n\nAnd the Winner Is........" + s.getWinner())

