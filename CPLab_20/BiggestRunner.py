"""
Lab 20.1        Biggest Double
--------
In this lab, you will write a program that  finds the
greatest of 4 numbers. You will input four floating
point numbers, and the program will tell you which one
is the biggest.
"""
from BiggestNumber import*
def main():
    """Test Cases"""
    run = BiggestNumber(4.5, 6.7, 7.8, 9.0)
    print(run)
    print("biggest = ", run.getBiggest(), "\n")

    run.setNumbers(14.51, 6.17, 71.8, 1.0)
    print(run)
    print("biggest = ", run.getBiggest(), "\n")

    """Create User Inputs...."""
    num1 = input("What is your 1st number: ")
    num2 = input("What is your 2nd number: ")
    num3 = input("What is your 3rd number: ")
    num4 = input("What is your 4th number: ")

    run.setNumbers(num1,num2,num3,num4)
    print(run)
    print("biggest = ", run.getBiggest(), "\n")
main()
