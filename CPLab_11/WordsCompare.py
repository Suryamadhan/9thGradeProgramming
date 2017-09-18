class WordsCompare:

    #Constructor
    def __init__(self, s1, s2,):
        self.word1=s1
        self.word2=s2

    def largestword(self):
       if self.word1 > self.word2:
           return self.word1

       if self.word1 < self.word2:
           return self.word2

    def smallestword(self):
        if self.word1 < self.word2:
            return self.word1

        if self.word1 > self.word2:
            return self.word2


    def __str__(self):
        return "According to the Oxford dictionary " + str(self.smallestword()) + " comes before " + str(self.largestword())+"."

