class BMI:
    def __init__(self, n="", h=0, w=0):
        self.name = n
        self.height = h
        self.weight = w
        self.bmi = 0

    def setValues(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def calcBmi(self):
        self.bmi = self.weight / (self.height * self.height)

    def __str__(self):
        return "<<<< " + self.name + " InFo >>>>" "\n" "Height: " + str(self.height) + " inches""\n" "Weight: " + str(self.weight) + " pounds""\n" "BMI: " + str(self.bmi)
    """Modifier: set new weight"""

    """calcBMI(): same formula as the original"""

    """__str__():
        return <<<< [name]'s Info: >>>>
               Height:[height]
               Weight:[weight]
               BMI:[bmi]
    """
