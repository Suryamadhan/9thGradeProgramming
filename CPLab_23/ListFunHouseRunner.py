"""
Lab 23.2        List Fun House
--------
In this lab, you will write a program takes an array and...
- prints the sum of values from @ start to @ stop
- counts the number of times val occurs in the list
- returns a copy of the list with all occurrences of val removed
"""

from ListFunHouse import *
def main():
    one = [7, 4, 10, 0, 1, 7, 6, 5, 3, 2, 9, 7]
    print(one)

    lfh = ListFunHouse(one)
    print("Sum of spots 3-6 = " + str(lfh.getSum(3, 6)))
    print("Sum of spots 2-9 = " + str(lfh.getSum(2, 9)))
    print("# of 4s = " + str(lfh.getCount(4)))
    print("# of 4s = " + str(lfh.getCount(7)))
    print("The list without 7s: " + str(lfh.removeVals(7)))

    two = [4,2,3,4,6,7,8,9,0,10,0,1,7,6,5,3,2,9,9,8,7]
    print (two)

    lfh.setList(two)
    print("Sum of spots 3-6 = " + str(lfh.getSum(3, 16)))
    print("Sum of spots 2-9 = " + str(lfh.getSum(2, 9)))
    print("# of 4s = " + str(lfh.getCount(0)))
    print("# of 4s = " + str(lfh.getCount(4)))
    print("The list without 7s: " + str(lfh.removeVals(7)))

main()