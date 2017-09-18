"""
Lab 20.2        First String
---------
This will be the object class for the Frist Sring lab.
"""
class FirstString:
    """Constructor..."""
    def __init__(self, a, b, c):
        self.one = a
        self.two = b
        self.three = c

    """Modifier...."""
    def setStrings(self, a, b, c):
        self.one = a
        self.two = b
        self.three = c


    """
    getFirst() function: compare the Strings with > or < to
    see which one would come first in the dictionary
    if one comes before two and three...
        return one
    if two comes before one and three...
        return two
    otherwise...
        return three
    """
    def getFirst(self):
        if self.one < self.two and self.one < self.three:
            return self.one
        if self.two < self.one and self.two < self.three:
            return self.two
        else:
            return self.three

    def __str__(self):
        return self.one + " " + self.two + " " + self.three
