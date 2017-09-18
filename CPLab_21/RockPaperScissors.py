"""
Lab 21.2        Rock Paper Scissors
---------
Object class for the Rock Paper Scissors lab.
"""

from random import randint

class RockPaperScissors:
        def __init__(self, pCh):
            self.playChoice = pCh
            self.compChoice = ""
            self.choice = randint(0, 3)
            self.winner = ""

            if self.choice == 0:
                self.compChoice = "R"
            elif self.choice == 1:
                self.compChoice = "P"
            else:
                self.compChoice = "S"

        def determineWinner(self):
            if self.compChoice == self.playChoice:
                return "Draw Game!"
            elif self.compChoice == "R" or self.compChoice == "r":
                if self.playChoice == "P" or self.playChoice == "p":
                    return ("!Player wins <<Paper Covers Rock>>!")
                else:
                    return ("!Computer wins <<Rock Breaks Scissors>>!")
            elif self.compChoice == "P" or self.compChoice == "p":
                if self.playChoice == "S" or self.playChoice == "s":
                    return ("!Player wins <<Scissors Cuts Paper>>!")
                else:
                    return ("!Computer wins <<Paper Covers Rock>>!")
            else:
                if self.playChoice == "R" or self.playChoice == "r":
                    return ("!Player wins <<Rock Breaks Scissors>>!")
                else:
                    return ( "!Computer wins <<Scissors Cuts Paper>>!")


        def __str__(self):
            output = ""
            output += "player had " +self.playChoice+ "\n"
            output += "Computer had " + self.compChoice
            return output