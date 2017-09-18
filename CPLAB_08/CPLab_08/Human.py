
class Human:
    def __init__(self, eC, hC, sC, h, w):
        self.eyeColor = eC
        self.hairColor = hC
        self.skinColor = sC
        self.height = h
        self.weight = w

    def setHrColor(self, hC):
        self.hairColor = hC

    def getEyeColor(self):
        return self.eyeColor
    def getHrColor(self):
        return self.hairColor
    def getSknColor(self):
        return self.skinColor
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight

    def main ():
        eC = input("What is your eye color? ")
        hC = input("What is your hair color? ")
        sC = input("What is your skin color? ")
        h = input("What is your height? ")
        w = input("What is your weight? ")

        print ("Your eye color is", eC)
        print ("Your hair color is", hC)
        print ("Your skin color is", sC)
        print ("Your height is", h)
        print ("Your weight is", w)

    main()