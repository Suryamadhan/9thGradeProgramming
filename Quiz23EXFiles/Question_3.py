class Down:
    def __init__(self, w):
        self.word = w
        self.down = ""

    def setWord(self, w):
        self.word = w
        self.down = ""

    def turnDown(self):
        for i in range(len(self.word), 0, -1):
            print(self.word[:i])


    def __str__(self):
        return self.down