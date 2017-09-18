"""
Lab 17.1        Digit Counter
---------
This is the object class for Digit Counter. Use
a for loop to finish CountDigits.
"""

class DigitCounter:
    def __init__(self, num):
        self.number = num


    """Modifier"""


    """Set variable [digits] to 0.
    while loop: number is greater than 0,
    add 1 to [digits] each time the loop runs
    divide number by ten to shave off the last digit."""
    def countDigits(self):
        num = self.number
        cnt = 0
        while num > 0:
            cnt += 1
            num = int(num / 10)
        return cnt