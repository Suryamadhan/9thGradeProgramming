"""
* APLab_15.1:       Cool Numbers
* -----------
* In this lab, you will write a program that looks for "cool"
    * numbers. Cool numbers are those that can be divided by 3, 4, 5, and
* 6, with a remainder of 1.
*
* Directions
* -----------
* You should be able to input a large number, and the program should
* tell you how many "cool" numbers are in it.
*
* Sample Input         Sample Output
* ------------        --------------
*      3095           There are 52 cool numbers in 3095
"""

from CoolNumbers import*

"""Test Case:
* Use these to help get your object class working" """
def main():

    nums = CoolNumbers(43589)
    nums.countCoolNumbers()
    print(nums)

    """Now comment out everything in the test case except the new
    * object, and create user input for the number. Add the
    * new number to the modifier (parameters) and print nums again."""

    Number = int(input("Designate a number that may be teeming with Cool Numbers(trademark): "))
    Surya = CoolNumbers(Number)
    Surya.setNum(Number)
    Surya.countCoolNumbers()
    print(Surya)
main()