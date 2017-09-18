"""
Lab 22.1        Instance Vars
---------
Object class for the Instance Vars lab
"""
class ListInstanceVars:
    def __init__(self, list):
        self.nums = []
        self.setNums(list)
    def setNums(self, list):
        self.nums = list.split(" ")
    def __str__(self):
        output = ""
        jj = 0
        for i in self.nums:
            output += str(i)
            if jj < len(self.nums)-1:
                output += ", "
            jj += 1
        return output

