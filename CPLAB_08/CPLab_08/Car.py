"""
Ex_02
In this exercise, you will be creating a car class
You must choose at least 4 properties to use as parameters
for your car objects. Set them as inputs, and print
your car's information.
"""
class Car:
    def __init__(self, p, i, e, t ):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t


    def getPaint(self):
        return self.paint
    def getInterior(self):
        return self.interior
    def getEngine(self):
        return self.engine
    def getTires(self):
        return self.tires

    def main():
        p = input("What color is your car? ")
        i = input("What kind of interior does your car have? ")
        e = input("What engine does your car have? ")
        t = input("What is your height? ")

        print ("Paint:   ", p)
        print ("Interior:", i)
        print ("Engine:  ", e)
        print ("Tires:   ", t)
    main()

