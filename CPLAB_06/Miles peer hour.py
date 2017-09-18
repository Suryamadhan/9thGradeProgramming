__author__ = 'Surya'
class MilesPerHour:
    #Constructor(params self, distance, hours, minutes)
    #instance variables (self.variable...)
    #set variables for distance, hours, and minutes = to param values
    #variable mph = 0
    def __init__(self, d =0, h =0, m =0):
        self.distance = d
        self.hours = h
        self.minutes = m
        #set variables for distance, hours, and minutes = to param values
        #variable mph = 0
    def setValues(self, d1, h1, m1):
        self.d = d1
        self.h = h1
        self.m = m1
        #Method to calculate the distance
    def calcMPH(self):
        self.mph = self.distance/(self.hours + self.minutes / 60.0)

        #Accessor
        #returns the distance value
    def getMPH(self):
        return self.mph

#main()method
def main():
    #get user inputs for distance, hours, and minutes
    dist = float (input("enter the distance Traveled:"))
    hrs = float(input("Enter the number of hours traveled: "))
    mins = float(input("Enter the number of minutes traveled:"))
    #instantiate a new MilesPerHour object (enter params to set data values)
    mph = MilesPerHour(dist, hrs, mins)
    mph.calcMPH()
    #run calcMPH

    #print the results, formatted nicely....
    #EX: 10 miles in 2 hours = 5 mph.

    #run the modifier (params to reset data values)
    #set distance, hours, and minutes = to param values3

    print("<<<<<<<<< USING THE MODIFIER >>>>>>>>")
    print("You are traveling", mph.getMPH(), "miles per hour")

    #print again

main()