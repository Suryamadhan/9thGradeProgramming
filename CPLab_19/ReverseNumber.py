"""
Lab 19.2        Reverse Number
---------
This will be the Object class for the Reverse Number lab
"""
class ReverseNumber:
    def __init__(self, num):
        self.number = num

    """Modifier..."""
    def setNumber(self,num):
        self.number = num

    """
    getReverse() function
    ----------------------
    declare variable [rev] = 0.
    declare variable [num] = [number]
    while loop: runs as long as [num] > 0....
        [rev] = int([rev] times 10 plus num % 10)
        divide [number] by 10*/
    return [rev]
    """
    def getReverse(self):
        rev = 0
        while(self.number > 0):
            rev = (10*rev)+self.number%10
            self.number //= 10
        return rev


    def __str__(self):
        return "If you reverse " + str(self.number)+" you get "+ str(self.getReverse())

