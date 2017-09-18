"""
 * CPLab_16.2:        Print Factors
 * -----------
 * In this lab, you will create a program that
 * returns the factors of a number that you enter.
"""
from PrintFactors import *

def main():

    """Test Case"""
    factors = PrintFactors(2152)
    factors = factors.__str__()
    print(factors)

    number = int(input("What is your number: "))
    Surya = PrintFactors(number)
    Surya = Surya.__str__()
    print(Surya)

    """Take user inputs....."""

main()

