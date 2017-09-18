class BMI:
    def __init__ (self, h=0, w=0):
        self.height = h
        self.weight = w
    
    def getBMI(self):
        bmi = (self.weight*703)/(self.height*self.height);
        return bmi;
