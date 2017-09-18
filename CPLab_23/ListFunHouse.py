"""
Lab 23.2        List Fun House
--------
Object class for List Fun House Lab
"""
class ListFunHouse:
    """Constructor"""
    def __init__(self, a1):
        self.setList(a1)

    """Add Modifier"""
    def setList(self, a1):
        self.myList = a1


    """getSum(): returns the sum of the values from
    myList @ start to @ stop.

    set sum = 0
    set i = start
    while loop: runs as long as i < length of myList and i <= stop.
        add myList @ i to sum
        add one to i
    return sum"""
    def getSum(self, start, stop):
        sum = 0
        i = start
        while i < len(self.myList) and i <= stop:
            sum += self.myList[i]
            i+=1
        return sum



    """getCount() returns the number of times val occurs in myList
    set count = 0
    for loop: from 0 to length of myList
        if myList @ i is equal to val
            add one to count
        return count"""
    def getCount(self, val):
        count = 0
        for i in range(0,len(self.myList)):
            if self.myList[i] == val:
                count += 1
            return count


    """returns a copy of myList with all occurences of val removed
    set new list "ret" to empty
    for loop: each item in myList:
        if item is not equal to val
            add item onto the end of ret
    return ret"""
    def removeVals(self, val):
        ret  =[]
        for i in self.myList:
            if i != val:
                ret += str(i)
        return ret

