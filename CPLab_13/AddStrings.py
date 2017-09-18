class AddStrings:
    def __init__(self,fn='',ln=''):
        self.firstname = fn
        self.lastname = ln
        self.sum = ""

    def setNames(self, fn, ln):
        self.firstname = fn
        self.lastname = ln
        self.sum = ""

    def getSum(self):
        self.sum = self.firstname + " " + self.lastname
        return self.sum

    def __str__(self):
        return "Your full name is " + self.getSum()



