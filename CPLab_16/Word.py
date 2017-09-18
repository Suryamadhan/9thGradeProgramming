"""
CPLab_14.2: Word Runner
-----------
Object class for the WordRunner
"""
class Word:
    def __init__(self,w):
        self.word = w
        self.back = ""

    def setWord(self,w):
        self.word = w
    """
    Constructor
    """

    """
    Modifier
    """

    """
    Get the first character of the word
    """
    def getFirstChar(self):
        return self.word[0:1]
        
    """
    Get the last character of the word
    """
    def getLastChar(self):
        return self.word[len(self.word)-1: len(self.word)]


    """
    for loop: from 0 to word length. Iterate up by 1
    Every time the loop runs....
    add the character at position i to back*/
    def getBackward(self):
    """
    def getBackward(self):
        for i in range(len(self.word)-1,-1,-1):
            self.back = self.back + self.word[i]
        return self.back


    def __str__(self):
        return "The first character of the word is... " + self.getFirstChar() + ". " + "\n" + "The last character of the word is... " + self.getLastChar() + ". " + "\n" + "The word backward is ..." + self.getBackward()
    """
    __str__() method
    """
