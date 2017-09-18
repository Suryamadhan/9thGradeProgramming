"""---------------------------------------------------------
* CPLab_14.3:      Multiplication Table
* ----------
* In this lab, you will create a multiplication
* table for a number. The object will take 2
* parameters: a number and a stop. The number by
* each of the factors of the stop, including the.
* stop. For example, The (3, 7) in the test cases
* below should multiply 3 times 1-7
*
* input            output
* -----           -------
* (3, 7)          multiplication table for 3
*                 1      3
*                 2      6
*                 3      9
*                 4     12
*                 5     15
*                 6     18
*                 7     21
--------------------------------------------------------"""

from MultTable import*

def main():
    """ Test cases - use these to make sure the
    object class works before going further."""
    test = MultTable(5, 5)
    test.printTable()

    number1 = int(input("What multiplication tables do you want: "))
    number2 = int(input("How many terms do you want in your tables: "))

    surya = MultTable(number1,number2)
    print(surya.printTable())

    """User Inputs:     <<<comment out the test cases>>>>
    * -------------
    * Create a Scanner input for the word, and use the
    * modifier on the "test" object to pass the new data
    * into test."""

main()
