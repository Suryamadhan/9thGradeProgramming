"""
CPLab_16.2      Print Factors
----------
This is the object class for 16.2
"""
class PrintFactors:
    def __init__(self, num):
        self.number = num
        self.factors = ""

    def setNum(self, num):
        self.number = num
        self.factors = ""
    """ for loop: from 1 to number. iterate up by 1
        Every time the loop runs...

        if i divides evenly into number...
        add i to the String [factors]. Hint: add a
        comma and space in between the factors."""

    def getFactors(self):
        for i in range(2,self.number+1,1):
            if self.number % i == 0:
                self.factors = self.factors + ", " + str(i)


    def __str__(self):
        self.getFactors()
        return "The factors of " + str(self.number) + " are " + "1" + str(self.factors)



