"""
Lab 20.1        Biggest Double
--------
This will be the object class for the Biggest Double lab.
"""
class BiggestNumber:
    def __init__(self, n1, n2, n3, n4):
        self.one = n1
        self.two = n2
        self.three = n3
        self.four = n4

    """Modifier...."""
    def setNumbers(self, n1, n2, n3, n4):
        self.one = n1
        self.two = n2
        self.three = n3
        self.four = n4

    """
    getBiggest() function: returns the greatest of the four
    input floating point numbers.
        if one is greater than two, three, and four
            return one
        if two is greater than one, three, and four
            return two
        if three is greater than one, two, and four
            return three
        otherwise...
            return three
    """
    def getBiggest(self):
        if self.one > self.two and self.one > self.three and self.one > self.four:
            return self.one
        if self.two > self.one and self.two > self.three and self.two > self.four:
            return self.two
        if self.three > self.one and self.three > self.two and self.three > self.four:
            return self.three
        if self.four > self.two and self.four > self.three and self.four > self.one:
            return self.four


    def __str__(self):
        return str(self.one) + ", " + str(self.two) + ", " + str(self.three) + ", " + str(self.four)
