"""
    Ex_01: GPA Printer
    Create a Grades class that calculates the points for each of the
    Grades objects.
"""

class Grades:
    def __init__(self,lg):
        self.lettergarde = lg


    def getGrade(self,lettergrade):
        self.lettergarde = self.gradepoint

    def calcPoints(self,lettergrade,gradepoint):
        if lettergrade == "A":
            self.gradepoint = 4
        elif lettergrade == "B":
            self.gradepoint = 3
        elif lettergrade == "C":
            self.gradepoint = 2
        elif lettergrade == "D":
            self.gradepoint = 1
        else:
            self.gradepoint = 0

    def getletterGrade(self):
        return self.gradepoint

