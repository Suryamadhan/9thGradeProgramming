"""
    APLab_16.3:      Prime Runner
 *- -----------
 *  In this lab you will create a program that tells
 *  you weather or not a number is prime. Remember: a
 *  prime number is one that is only divisible by 1 and
 *  itself.
"""

from Prime import *

def main():
    #test = Prime(5)
    #print(test)

    number = int(input("What is your number: "))
    Surya = Prime(number)
    Surya = Surya.__str__()
    print(Surya)


main()