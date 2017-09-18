"""========================================================
Lab_24.1        List Stats
---------
This will be the object class for the List Stats lab
=========================================================="""
class ListStats:
    """Constructor..."""
    def __init__(self, sList):
        self.list = []
        self.setList(sList)


    def setList(self,sList):
        for n in sList.split():
            self.list += n

    """================= setList(self, sList) ======================
    for loop: each item n in sList.split()
        add n to self.list
    =============================================================="""

    def getNumGroupsOfSize(self,size):
        cnt = 0
        count = 0
        curr = self.list[0]

        for i in range(0,len(self.list)):
            if self.list[i] == curr:
                count += 1
            elif count >= size:
                cnt+= 1
                count = 1
                curr = self.list[i]
            elif self.list[i] != curr and count < size:
                curr = self.list[i]
                count += 1
        if count >= size:
            cnt += 1
        return cnt
    """============== getNumGroupsOfSize(self, size) ==================
    declare variables...
    Set cnt to 0
    Set count to 0
    Set curr = self.list @ 0

    for loop: from 0 to length of list
        if list @ i is equal to curr...
            add 1 to count
        else if count is >= size...
            add 1 to cnt
            set count to 1
            set curr to list @ i
        else if list @ i is not curr and count is less than size...
            set curr to list @ i
            set count to 1
    if count is greater than or equal to size...
        add 1 to cnt
    return cnt
    ================================================================"""


    """__str__() function"""
    def __str__(self):
            return str(self.list)
