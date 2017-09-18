"""
Lab 23.2       List Fun House two
--------
This lab tells you weather a list is in ascending or
descending order, and counts the number of times an input
number occurs in the list. It also contains a getCountValues()
function that will print out all the values in the list that
are greater than the input value.
"""


from ListFunHouseTwo import *
def main():
    one = [1,2,3,4,5,6,7,8,9,10]
    two = [1,2,3,9,11,20,30]
    three = [9,8,7,6,5,4,3,2,1-1,-2]

    print(one)

    lfh2 = ListFunHouseTwo(one)
    print("Is going up? ", lfh2.goingUp())
    print("Is goint down? ", lfh2.goingDown())
    newOne = lfh2.getCountValues(7, 2)
    print("the first 7 values greater than 2: ", newOne)

    print(two)
    lfh2.setList(two)
    print("Is going up? ", lfh2.goingUp())
    print("Is goint down? ", lfh2.goingDown())
    newTwo = lfh2.getCountValues(5, 6)
    print("the first 5 values greater than 6: ", newTwo)


main()