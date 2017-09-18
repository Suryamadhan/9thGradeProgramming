"""
CPLab_15.1:     Cool Numbers
-----------
This is the object class for the CoolNumbers lab.
"""
class CoolNumbers:
    def __init__(self, num):
        self.count = 0
        self.number = num

    def setNum(self, num):
        self.count = 0
        self.number = num

    """ isCoolNumber() will tell you if your number is "cool",
    meaning it meets the conditions below. """
    def isCoolNumber(self, num):
        return num % 3 == 1 & num % 4 == 1 & num % 5 == 1 & num % 6 == 1


    def countCoolNumbers(self) :
        for i in range(0, self.number):
            CoolNumbers.isCoolNumber(self,i)
            if CoolNumbers.isCoolNumber(self,i) == True:
                self.count += 1



    def __str__(self):
        return "There are " + str(self.count) + " cool numbers in " + str(self.number)


