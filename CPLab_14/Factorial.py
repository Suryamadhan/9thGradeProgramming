"""
* APLab_14.4:      Factorial
*------------
* This is the object class for lab 14.4. It
* should create a Factorial object.
"""

class Factorial:
    """Constructor"""
    def __init__(self, num):
        self.number = num
        self.Factorial = 1

    """Modifier"""
    def setNum(self, num):
        self.number = num

    """Accessor"""
    def getNum(self):
        return self.number

    """Calculate the factorial value:
     * Start with a variable "factorial" to hold the factorial value.
     * for loop: from i = 1 to number+1 (exclusive). Multiply the
     * factorial by i each time the loop runs."""
    def getFactorial(self):
        for i in range(self.number,0,-1):
            self.Factorial = self.Factorial * i
        return self.Factorial


    """__str___() function"""
    def __str__(self):
        return "!" + str(self.getNum()) + " = " + str(self.getFactorial())