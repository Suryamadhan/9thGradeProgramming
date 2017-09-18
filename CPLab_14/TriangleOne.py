"""-------------------------------------------------
* CPLab_14.2:  Triangle
* -----------
* Object class for lab 14.2: Creates a TriangleOne
* object.
-----------------------------------------------------"""

class TriangleOne:
    """Constructor"""
    def __init__(self, wrd):
        self.word = wrd

    """Modifier"""
    def setWord(self, wrd):
        self.word = wrd

    """for loop: from i = length of word - 0. Increment
     * i down by 1. Print a  substring of the word from 0
     * to i each time the loop runs."""
    def print(self):
        for i in range(0, len(self.word)):
            print(self.word[0: len(self.word) - i])





