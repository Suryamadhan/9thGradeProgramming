"""Question 1: Unresolved Reference.."""
class Name:
    def __init__(self, fN, lN, nN):
        self.firstName = fN
        self.lastName = lN
        self.nickName = nN

    def setNames(self, fN, lN, nN):
        self.firstName = fN
        self.lastName = lN
        self.nickName = nN

    def __str__(self):
        name = self.firstName + "\n" \
        + self.lastName + "\n" \
        + self.nickName

        return name