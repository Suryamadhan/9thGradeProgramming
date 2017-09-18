"""
CPLab_14.1:     Box
-----------
This is the object class for lab 14.1. It
should create a Box object.

"""

class Box:
    """Constructor"""
    def __init__(self, wrd=""):
        self.word = wrd

    """Modifier"""
    def setWord(self, wrd):
        self.word = wrd

    def getWord(self):
        return self.word


    """for loop: from i = 0 - length of word
    print word each time the loop runs."""
    def __str__(self):
        return str(self.getWord())




#for na in range (4, 0, -1):
 #   print("Na")
#print()
#print("Remember this song?")
#or na in range (len(s), 0, -1):
 #   print("Na")
#print()
