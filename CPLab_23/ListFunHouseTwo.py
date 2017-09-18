"""
Lab 23.2    List Fun House
---------
Object class for List Fun House lab
"""

class ListFunHouseTwo:
    """Constructor"""
    def __init__(self, ml):
        self.setList(ml)

    def setList(self, ml):
        self.myList = ml

    """Add Modifier"""


    """goingUp() returns true if all numbers in the
    list are in ascending order. [1, 2, 3, 4...]

    for loop: from 1 to length of myList
        if myList @ i-1 > myList @ i
            return false
        otherwise --> return true"""
    def goingUp(self):
        for i in range(1,len(self.myList)):
            if self.myList[i -1] > self.myList[i]:
                return False
            else:
                return True


    """goingUp() returns true if all numbers in the
    list are in descending order. [5, 4, 3, 2...]

    for loop: from 1 to length of myList
        if myList @ i-1 < myList @ i
            return false
        otherwise --> return true"""
    def goingDown(self):
        for i in range(1,len(self.myList)):
            if self.myList[i -1] < self.myList[i]:
                return False
            else:
                return True

    """getCountValues() will return an array that contains
    count number of values that ar larger than parameter x

    declare a list "ret"
    set variable i to 0
    while loop: from 0 to count:
    run as long as i <  length of myList
        if myList @ j > x
            add myList @ j to the end of ret

        add one to i
    return ret
        """
    def getCountValues(self, count, x):
        ret = []
        i = 0
        while i < len(self.myList):
            if self.myList[i] > x:
                ret += str(self.myList[i])

            i+=1
        return ret

