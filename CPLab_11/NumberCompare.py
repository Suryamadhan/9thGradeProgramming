class NumberCompare:
    def __init__(self, n1, n2):
        self.one = n1
        self.two = n2

    def getLargest(self):
        if self.one > self.two:
            return self.one
        if self.two > self.one:
            return self.two

    def getSmallest(self):
        if self.one > self.two:
            return self.two
        if self.two > self.one:
            return self.one

    def __str__(self):
        return self.getLargest() + " is a greater number than " + self.getSmallest() + "." "\n" + "In other words...." + "\n" + self.getSmallest() + " is a smaller number than " + self.getLargest() + "."

