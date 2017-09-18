class FirstAndLast:
    """Constructor: """
    def __init__(self, wrd):
        self.word = wrd

    """Modifier: sets the instance variable =
     the input word."""
    def setWord(self, wrd):
        self.word = wrd

    """Use the object[x, y] function to return the
    first letter of the input word."""
    def getFirst(self):
        return self.word[0:1]


    """Use the object[x, y] function to return the
    last letter of the input word. You will need to
    use the word length to find the top of the
    range. """
    def getLast(self):
        return self.word[len(self.word)-1: len(self.word)]

    """Use the __str__() method to return our first and last
    Letters in printable output:

    <<<<<< [input word]>>>>
    first letter:: [output of getFirst()]
    last letter:: [output of getLast()]
    """
    def __str__(self):
        return "The first letter of the name is " + self.getFirst() + "." + "\n" + "The last letter of the name is " + self.getLast()
