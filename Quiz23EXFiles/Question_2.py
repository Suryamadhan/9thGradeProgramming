class Table:
    def __init__(self, num, stp):
        self.number = num
        self.stop = stp

    def setTable(self, num, stp):
        self.number = num
        self.stop = stp

    def printTable(self):
        print("Multiplication table for ", self.number)
        for i in range (1, self.stop+1):
            print(i, "%7d" % (i*self.number))