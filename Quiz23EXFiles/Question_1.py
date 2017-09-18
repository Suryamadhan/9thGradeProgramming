class Cube:
    def __init__(self, h, w, d):
        self.height = h
        self.weight = w
        self.depth = d

    def setVals(self, h, w, d):
        self.height = h
        self.weight = w
        self.depth = d

    def getVolume(self):
        volume = self.height * self.weight * self.depth
        return volume