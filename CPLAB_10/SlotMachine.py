"""
EX_03: Slot Machines
You are writing a program for a casino to randomize
which slot machine should hit a jackpot. Make a class
that has the following...
"""
import random
class Slotmachine:
    def __init__(self, n, jp = ""):
        self.name = n
        self.jackpot = jp

    def hitJackpot(self):
        self.jackpot = random.randint(1,100)
        if self.jackpot == 1:
            self.jackpot = "Hit!"
        else:
            self.jackpot = "Operating normally"

    def __str__(self):
        return str(self.name) + ": " + str(self.jackpot)

def main():
    grade1 = input("What grade did you achieve in your first assignment? ")
    gradeo = Slotmachine(grade1)
    gradeo.calcPoints(gradeo.getGrade(grade1))
    print(gradeo)
main()