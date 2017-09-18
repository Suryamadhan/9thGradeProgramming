"""
CPLab_15.2:      Greatest Common Denominator
-----------
This is the object class for the GCD lab.
"""
class GCD:
    def __init__(self, x, y):
        self.one = x
        self.two = y
        self.gcd = 0
        self.top = 0

    def setNums(self, x, y):
        self.one = x
        self.two = y
        self.gcd = 0

    """
    * Start with the "top" variable below. This variable holds
    * the greater of numbers one and two.
    * for loop: from "top" to 1, increment i down by 1. Every
    * time the loop runs...
    *
    * if i divides evenly into one and two, set gcd to i and
    * then break."""
    def getGCD(self):
        """The greater of [one] and [two]"""
        self.top = max(self.one, self.two)
        for i in range(self.top, 1, -1):
            if self.one % i == 0 and self.two % i == 0:
                self.gcd = i
                break


    """Return "The GCD of [one] and [two] is [gcd]"""
    def __str__(self):
        return str(self.gcd)