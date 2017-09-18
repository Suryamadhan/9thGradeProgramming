class Marriage:
    """Constructor: """
    def __init__(self, s1, s2):
        self.spouse1 = s1
        self.spouse2 = s2

    """ Modifier: """
    def setNames(self, s1, s2):
        self.spouse1 = s1
        self.spouse2 = s2

    """Returns the value of the first name of
    spouse1, the person taking a new last name.
    You will need to return the value of our
    spouse1 from 0 to the first whitespace.(Hint: Use
     range slicing[] and index together. """
    def getFirstspouse1(self):
        return self.spouse1[ : self.spouse1.index(" ")]
    def getFirstspose2(self):
        return self.spouse2[ : self.spouse2.index(" ")]


    """This method will return the last name that is being taken by the spouse1.
    You will need to return the value of spouse1(String) from 0 to the first space )"""
    def getLastspouse1(self):
        return self.spouse1[self.spouse1.index(" "):]
    def getLastspouse2(self):
        return self.spouse2[self.spouse2.index(" "):]

    """The toString should return the value of getFirst() and getLast()
    * together. With the test case, the output should look like the
    * following:
    *
    * If Sally Baker marries Arnold Palmer.....
    * Sally's name wil be Sally Palmer"""

    def __str__(self):
        return "If " +  self.spouse1+ " marries " + self.spouse2 + "..."+ "\n" + self.getFirstspouse1() + "'s name will become " + self.getFirstspouse1() + " " +self.getLastspouse2()