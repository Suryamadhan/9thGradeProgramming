"""
Lab 18.2
--------
This lab isolates the digits in a number and adds them
together to get the sum. Your only work will be in the
object class.
"""

from DigitAdder import *

def main():

    """this is an array. You don't need to know how this works
      yet. It's just a test class for you to use."""
    cases = [234, 10000, 111, 9005, 84645,8547,123456789]
    sum = DigitAdder()

    for i in range (0, len(cases)):
        sum.setNum(cases[i])
        print(sum.sumDigits(), " is the sum of the digits in ", cases[i], "\n")

    """No need for user inputs. Just use the test case."""
main()