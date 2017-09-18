class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def setVals(self, b, h):
        self.base = b
        self.height = h

    def getArea(self):
        area = 0.5 * (self.base * self.height)
        return area
