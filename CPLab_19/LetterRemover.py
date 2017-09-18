"""
Lab 19.1        Letter Remover
--------
This will be the Object class for the LetterRemover lab
"""
class LetterRemover:
    def __init__(self, stce, lF):
        self.sentence = stce
        self.lookFor = lF

    def setRemover(self,stce, lF):
        self.sentence = stce
        self.lookFor = lF

    """Modifier..."""


    """
    removeLetters() function
    ------------------------
    use str.replace() to replace lookFor with an empty
    string ("").
    """
    def removeLetters(self):
        newstr = self.sentence.replace(self.lookFor,"")
        return newstr

    def __str__(self):
        return str(self.sentence) + " - letter to remove " + str(self.lookFor) +"\n"+str(self.removeLetters())
