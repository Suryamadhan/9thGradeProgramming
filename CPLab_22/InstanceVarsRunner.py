"""
Lab 22.1        Instance Vars
---------
In this lab, you will add the values from
a String to an array and then print the values
from the array properly separated by commas
"""
from ListInstanceVars import *
def main():
    test = ListInstanceVars("1 2 3 4 5 6 7 8 9 10")
    print(test)

    test.setNums("3 4 5 6 7 8 9 1 2 0")
    print(test)
main()
