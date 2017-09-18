__author__ = 'Surya'
class GetSs:
    def __init__(self, chk):
        self.check = chk
        self.count = 0

    def setCheck(self, chk):
        self.check = chk
        self.count = 0

    def countSs(self):
        for i in range(0, len(self.check)):
            if self.check[i] == "s":
                self.count += 1

    def __str__(self):
        self.countSs()
        return "The String " + self.check + " contains " + str(self.count) + " s's."