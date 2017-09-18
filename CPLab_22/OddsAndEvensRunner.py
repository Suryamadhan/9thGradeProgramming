"""
Lab 22.3      Odds And Evens
---------
In this lab, you will write a program that takes
an array as an input, counts the odds and evens, and
returns the even numbers and the odd numbers in new
separate arrays.
"""

from OddsAndEvens import *

def main():
    list1 = "2, 4, 6, 8, 10, 12, 14"
    test = OddsAndEvens(list1)
    print(test)

    list2 = "1, 2, 3, 4, 5, 6, 7, 8, 9"
    test.setNums(list2)
    print(test)

main()
