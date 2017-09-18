"""
Lab 22.2        List Count
---------
In this lab, you will write a program that counts the
number of instances of an input number in an array. for
example, the array [3, 5, 3, 4] contains 2 instances of
the number 3.
"""
from ListCount import *
def main():
    nums = [7, 7, 1, 7, 8, 7, 4, 3, 7, 9, 8]
    val = 7
    object = ListCount(nums, val)
    print(object)

main()