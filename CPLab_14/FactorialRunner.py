"""
* APLab_14.4: 		Factorial
*------------
* Factorials are a simple concept from Algebra. A
* factorial of a number n, or "!n" is the product
* of all its factors. Therefore "!n" is the product
* of all the numbers 1 to n. In this lab, you will
* write a loop that calculates the factorial of an
* input number.
*
* For example, 5 in the test case below will produce
* 1*2*3*4*5, or 120
*
* input            output
*-------          -------
*  5              !5 = 120
----------------------------------------------------"""

from Factorial import*

def main():
    """ Test cases - use these to make sure the
     object class works before going further."""
    test = Factorial(5)
    print(test)

    number = int(input("What is your number: "))
    surya = Factorial(number)
    print(surya)

    """User Inputs:     <<<comment out the test cases>>>>
    * -------------
    * Create a Scanner input for the word, and use the
    * modifier on the "test" object to pass the new data
    * into test."""


main()