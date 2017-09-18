"""
* CPLab_12.2
* -------------------------
*
* Lab Goal :
* -----------
* This lab was designed to teach you more about objects
* and the String class.
*
* Lab Description :
* -----------------
* Create a program that takes in one word as String input
* and will output the first and last letters of that word.
*
*
* Sample Input :                   Sample Output :
* ---------------                  ---------------------
* Hello                            word :: Hello
* World                            first letter :: H
*                                  last letter :: o
*
*                                   word :: World
*                                  first letter :: W
*                                  last letter :: d
====================================================================================="""

from FirstAndLast import*

def recalculate():
    choice = input("Would you like to run this program again: ")
    if choice == "yes":
        main()
    else:
        print("Thank you for using Surya's program.")
def main():


    fname = input("What is your first name: ")

    Surya = FirstAndLast(fname)
    Surya = Surya.__str__()

    print (Surya)
    recalculate()

    """Now take user input for word. You can use the
    Modifier on the existing object to enter new
    data and recalculate. """

    """Now take user input for the word"""
    """Remember: You can input the word to the modifier on the
    existing object. No need to create a new object."""


main()
