"""Question 5: Missing a letter..."""
class Down:
    def __init__(self, w):
        self.word = w
        self.down = ""

    def setWord(self, w):
        self.word = w
        self.down = ""

    def turnDown(self):
        for i in range(len(self.word)-1, -1, -1):
            print(self.word[i:])
            i += 1

    def __str__(self):
        return self.down
