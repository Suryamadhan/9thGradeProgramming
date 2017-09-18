class TotalX:
    def __init__(self, w):
        self.word = w
        self.count = 0

    def setWord(self, w):
        self.word = w
        self.count = 0

    def totalXs(self):
        for i in range(len(self.word)-1, -1, -1):
            if self.word[i] == "a" or self.word[i] == "A":
                self.count += 1

    def __str__(self):
        return "There are " + str(self.count) + " As in " + str(self.word)