"""
Lab 17.1        Digit Counter
---------
This lab counts the digits on the input number. You will
be using while loops
"""
from DigitCounter import *

def main():
    """Test Case"""
    numDigits = DigitCounter(34567)
    #print("There are ", numDigits.countDigits(), " digits in ", 34567)

    number = int(input("What is your number:"))
    surya = DigitCounter(number)
    print("There are ", surya.countDigits(), " digits in ", number)

    """Create inputs for your number
    Prompt the user for an integer and plug the integer into
    the modifier.
    print your results from countDigits."""
main()