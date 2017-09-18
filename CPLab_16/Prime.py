"""
CPLab_16.3:      Prime
----------
This is the object class for the Prime lab.
"""
import math
class Prime:
    def __init__(self, num):
        self.number = num

    def setNum(self, num):
        self.number = num


    def isPrime(self):
        for i in range(2,self.number):
            if self.number > 0:
                if self.number % i ==0:
                    return str(self.number) + " is not a prime number."
                else:
                    return str(self.number) + " is a prime number."
            else:
                return str(self.number) + " is not a prime number."


    def __str__(self):
        return self.isPrime()
