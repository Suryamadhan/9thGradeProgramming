"""
Lab 22.3      Odds And Evens
---------
Object class for the Odds And Evens lab
"""
class OddsAndEvens:
    def __init__(self, myL):
        self.odds = []
        self.evens = []
        self.myList = myL.split(", ")



    def setNums(self, myL):
        self.odds = []
        self.evens = []
        self.myList = myL.split(", ")


    def countEm(self, odd):
        count = 0
        for i in self.myList:
            if odd == True:
                if int(i) % 2 ==1:
                    count += 1
            if odd == False:
                if int(i) % 2 ==0:
                    count += 1
        return count


    def getEvens(self):
        for i in self.myList:
            if int(i) % 2 == 0:
                self.evens.append(str(i))





    def getOdds(self):
        for i in self.myList:
            if int(i) % 2 == 1:
                self.odds.append(str(i))


    def __str__(self):
        self.getOdds()
        self.getEvens()
        return "\nOdds and Evens: " + str(self.myList) + "\n" \
               "----------------------------------------------------------------\n" \
               "Number of odds: " + str(self.countEm(False)) + "\n" \
                "Number of evens: " + str(self.countEm(True)) + "\n" \
                "Odd Numbers: " + str(self.odds) +"\n" \
                "Even Numbers: " + str(self.evens)


