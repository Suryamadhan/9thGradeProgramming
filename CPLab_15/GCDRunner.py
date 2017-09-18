"""
* APLab_15.2:       Greatest Common Denominator
* -----------
* In this lab, you will create a program that takes two input
* numbers, and finds their greatest common denominator. Your
* finished program should take two input numbers, and print the
* gcd of the two inputs. """

from GCD import*


from GCD import*

"""Test Case:
* Use these to help get your object class working" """
def main():
    test = GCD(5, 25)
    test.getGCD()
    print(test)
    Number1 = int(input("Select a number: "))
    Number2 = int(input("Select another number: "))
    test.setNums(Number1,Number2)
    test.getGCD()
    print("The greatest common denominator is...." + str(test))
main()

