import math


class Circle:
    def __init__(self, r=0):
        self.radius = r
        self.pi = math.pi



    def setValues(self, r1=0):
        self.r = r1

    def calcCircle(self):
        self.circle = self.pi * self.radius**2

    def getCircle(self):
        return self.circle