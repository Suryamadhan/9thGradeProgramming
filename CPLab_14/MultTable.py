"""
CPLab_14.3:     Multiplication Table
------------
This will be the object class for lab 14.1.
It should create a MultTable object.
"""

class MultTable:
    """Constructor"""
    def __init__(self, num, stp):
        self.number = num
        self.stop = stp
        self.mult = 1

    """Modifier"""
    def setTable(self, num, stp):
        self.number = num
        self.stop = stp

    """for loop: from i = 1 - stop. Increment i by 1.
     * Print:  print(i, "%7d" % (i*self.number))
     * every time the loop runs."""
    def printTable(self):
        for i in range(1,self.stop+1,1):
            self.mult = self.number * i
            print(str(i) + "  " + str(self.mult))
