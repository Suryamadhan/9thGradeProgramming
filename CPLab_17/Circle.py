import math

class Circle(object):
        def __init__(self, rad=0):
                self.rad = rad
                self.pi = math.pi
                self.area = 0

        def calcArea(self):
                self.area = (self.rad * self.rad)*(self.pi)
                return self.area

        def printstatement(self):
                print("The Area of the circle is.... = " + str(self.area))

