class NumberMult:
    def __init__(self, n1, n2):
        self.one = n1
        self.two = n2
        self.sum = 0

    def setNums(self, n1, n2):
        self.one = n1
        self.two = n2
        self.sum = 0

    def addNums(self):
        self.sum = self.one * self.two

    def __str__(self):
        return str(self.sum)