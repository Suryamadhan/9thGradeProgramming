"""
Lab 22.2        List Count
---------
Object class for the List Count lab
"""
class ListCount:
    def __init__(self, mL, v):
        self.myList = mL
        self.val = v
        self.count = 0

    def countIt(self):
        for i in self.myList:
            if i == self.val:
                self.count += 1


    def __str__(self):
        self.countIt()
        output = ""
        jj = 0
        for i in self.myList:
            output += str(i)
            if jj < len(self.myList)-1:
                output += ", "
            jj += 1
        return "\nCounting the 7s in....\n" \
                    "-----------------------------\n" \
                    "" + output + "\n" \
                    "Number of 7s:\t" + str(self.count)

