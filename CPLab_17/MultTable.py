class Table:
    def __init__(self, num, stp):
        self.number = num
        self.stop = stp+1

    def setTable(self, num, stp):
        self.number = num
        self.stop = stp +1

    def printTable(self):
        print("Multiplication table for ", self.number)
        for i in range (1, self.stop):
            print(i, "%7d" % (i*self.number))
