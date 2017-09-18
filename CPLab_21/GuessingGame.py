"""
Lab 21.2        Guessing Game
--------
Object class for the Guessing Game lab.

"""
from random import randint

class GuessingGame:
    def __init__(self, stop):
        self.number = stop
        self.num = randint(1, self.number)
        self.guess = 0
        self.guessCount = 0

    def playGame(self):
        while self.guess != self.num:
            self.guess = 0
            while self.guess <= 0 or self.guess > self.number:
                self.guess = int(input("Please enter a number between 1 and " + str(self.number)))
                if self.guess <=0 or self.guess> self.number:
                    return ("number out of range!")
            self.guessCount +=1
        return ("It took " + str(self.guess)+" guesses to guess " +str(self.num))

    """
    while self.guess is not = self.num
        self.guess = 0
        while self.guess <= 0 or > self.number
            self.guess = user input: "Please enter a number between 1 and [str]"
            if self.gues is <= 0 or > self.number
            print "number out of range!"
        add 1 to self.guessCount
    print "It took [self.guessCount] guesses to guess [self.num]"
    """













