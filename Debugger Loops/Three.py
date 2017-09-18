"""Question 3: Division by Zero error.."""
class FactorCounter:
    def __init__(self, num):
        self.number = num
        self.count = 0

    def setNum(self, num):
        self.number = num
        self.count = 0

    def countFactors(self):
        for i in range(1, self.number):
            if self.number % i == 0:
                self.count += 1

    def __str__(self):
        return "The number " + str(self.number) + " has " + str(self.count) + " factors."