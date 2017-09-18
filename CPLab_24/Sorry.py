import random
class Sorry:
    def __init__(self):
        self.track = []
        for i in range(0,18):
            self.track.append(0)
        self.one = random.randint(1, 7)
        self.two = random.randint(1, 7)

        if self.one == self.two:
            self.two = random.randint(1, 7)

        self.oneCount = 0
        self.twoCount = 0
        self.turn = random.randint(1, 3)

        self.track[self.one] = 1
        self.track[self.two] = 2

    def play(self):
        if self.getWinner() != "":
            return False
        else:
            dist = random.randint(1,7)
            if self.turn == 1:
                if self.one + dist >= 18:
                    self.track[self.one] = 0
                    self.one = 0
                    self.track[self.one] = 0
                    self.oneCount += 1
                else:
                    self.track[self.one] = 0
                    self.one += dist
                    self.track[self.one] = 1

                    if self.one == self.two:
                        self.two = 0
                    self.turn = 2
            else:
                if self.two + dist >= 18:
                    self.track[self.two] = 0
                    self.two = 0
                    self.track[self.two] = 2
                    self.twoCount += 1
                else:
                    self.track[self.two] = 0
                    self.two += dist
                    self.track[self.two] = 2

                    if self.two == self.one:
                        self.one = 0

                    self.turn = 1
        return True


    def getWinner(self):
        if self.oneCount == 5:
            return "1"
        if self.twoCount == 5:
            return "2"
        else:
            return ""



    """
    ================ Constructor ========================
        New Array track
        for loop: from 0 to 18
            add 18 0s to track[] array

        Variable [one] = random number between 1 and 6
        Variable [one] = random number between 1 and 6

        if [one] and [two] are equal
            set [two] new random number between 1 and 6

        Variable [oneCount] = 0
        Variable [twoCount] = 0
        Variable [turn] = random number 1 or 2

        Set track @ [one] = 1
        Set track @ [two] = 2
    =====================================================
    """


    """
    ===================== play() =================================
        if getWinner() returns anything but an empty String...
            return False

        Otherwise....
            New Variable [dist] = random number between 1 and 6
            if [turn] is equal to 1
                if [one] + [dist] >= 18
                    set [track] @ [one] to 0
                    set [one] to 0
                    set [track] @ [one] to 0
                    add 1 to [oneCount]
                otherwise...
                    set [track] @ [one] to 0
                    add [dist] to [one]
                    set [track] @ [one] to 1

                    if [one] is equal to [two]
                        set [two] to 0

                    set [turn] to 2

            otherwise....
                if [two] + [dist] >= 18
                    set [track] @ [two] to 0
                    set [two] to 0
                    set [track] @ [two] to 2
                    add 1 to [twoCount]
                otherwise...
                    set [track] @ [two] to 0
                    add [dist] to [two]
                    set [track] @ [two] to 2

                    if [two] and [one] are equal...
                        set [one] to 0

                    set [turn] to 1

        return True
    ================================================================
    """

    """
    ===================== getWinner() ====================
        if [oneCount] equals 5
            return "1"
        if [twoCount] equals 5
            return "2"
        otherwise...
            return ""
    =======================================================
    """


    def __str__(self):
        return str(self.track) + " one count = " + str(self.oneCount) + " | twoCount = " + str(self.twoCount)
