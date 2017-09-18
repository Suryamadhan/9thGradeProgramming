"""
Exercise_02

In this lab, you will write an object-oriented program that
calculates the distance between 2 points on a graph. You
should be able to input coordinates and output the distance.
"""

import math

class Distance:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.xOne=x1
        self.yOne=y1
        self.xTwo=x2
        self.yTwo=y2
        #Constructor (params self, x1, y1, x2, y2)



        #set instance variables to param values
        #integers xOne, yOne, xTwo, yTwo
        #double distance
    def set (self, a, b, c, d):
        self.x1=a
        self.y1=b
        self.x2=c
        self.y2=d


    #Modifier to reset coordinates

    def calcDistance(self):
        self.distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne));

    #Accessor to return distance
    def getDistance(self):
        return self.distance

#main() method
def main():
    #take in user input for x1, y1, x2, and y2
    x1 = float(input("What is x1: "))
    y1 = float(input("What is y1: "))
    x2 = float(input("What is x2: "))
    y2 = float(input("What is y2: "))


    #new Distance object
    dist = Distance(x1, y1, x2, y2)
    dist.calcDistance()
    #set coordinates on new object

    #run calcDistance()
    #print the distance with a label and number formatting
    #EX: distance = 22.35

    print("<<<<<<<<< USING THE MODIFIER >>>>>>>>")
    print("Your Answer is", dist.getDistance())


main()

