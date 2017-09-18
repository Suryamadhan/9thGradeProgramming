"""
CPLab_15.3:          Vowel Counter
-----------
This is the object class for the VowelCounter lab.
"""
class VowelCounter:

    """Constructor"""
    def __init__(self, wrd):
        self.word = wrd
        self.found = 0
        self.vowels = "aeiouAEIOU"

    """Modifier"""
    def setWord(self, wrd):
        self.word = wrd
        self.found = 0

    """for loop: from 0 to length of [word]. For each letter (word[i]),
    check if it is contained in [vowels]. Add 1 to [found] every letter
     found in [vowels]"""

    def getNumberVowels(self):
        for i in range(0, len(self.word)):
            if self.word[i] in self.vowels:
                self.found += 1
        return self.found




    """__str__(): return "The String [word] contains [found] vowels. """
    def __str__(self):
        return "There are " +  str(self.getNumberVowels()) + " vowels in the word you entered."