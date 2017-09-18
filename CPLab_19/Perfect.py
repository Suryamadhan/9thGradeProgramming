"""
Lab 19.3        Perfect
--------
This will be the object class for the Perfect lab.
"""

class Perfect:
    def __init__(self, num):
        self.number = num

    def setNum(self,num):
        self.number = num

    """Modifier..."""


    """
    isPerfect() function
    ---------------------
    Declare and int [num] = 1 and [sum] = 0
    while loop: runs as long as [num] < [number]....
        if [num] divides evenly into [number]...
            add [num] to [sum]
        add 1 to [num]
    if [sum] is equal to [number]...
        return true
    return false otherwise
    """
    def isPerfect(self):
        num = 1
        sum = 0
        while num < self.number:
            if self.number % num == 0:
                sum = sum + num
            num = num + 1
        if sum == self.number + 1:
            return str(self.number) + " is perfect number\n"
        else:
            return "" + str(self.number) + " is not perfect number\n"


    def __str__(self):
        return self.isPerfect()
