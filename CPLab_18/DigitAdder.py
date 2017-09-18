"""
Lab 18.2
--------
This is the object class for Digit Adder. Use a while loop
to finish the sumDigits() function.
"""
class DigitAdder:
    def __init__(self, num =0):
        self.number = num

    def setNum(self,num):
        self.number = num





    """Modifier"""

    """initialize a variable [sum] to zero.
    while loop: runs as long as [number] is greater than 0.
    now use modulus to get the last digit of "num" and add this
    to the value of [sum]. Then divide [number] by ten to shave off
    the last digit."""
    def sumDigits(self):
        num = self.number
        sum = 0
        while num > 0:
            sum += num % 10
            num = int(num / 10)
        return sum