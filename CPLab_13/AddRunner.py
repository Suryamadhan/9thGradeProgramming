"""==============================================================================================
 * CPLab_12.1
 *
 * Lab Goal :
 * ----------
 * This lab was designed to teach you more about objects and the String class.
 *
 * Lab Description :
 * -----------------
 * This program concatenates two Strings together. Finish
 * writing the code and set up user inputs.
 *
 * Example Input:		Example Output:
 * --------------		---------------
 * Super Man			Superman
 * Thunder Man			Thunderman
 *
=================================================================================================="""
from AddStrings import*

def main():
    demo = AddStrings("Hello","World")
    demo.getSum()
    print(demo)

    fname = input("What's your first name: ")
    lname = input("What's your last name: ")

    surya = AddStrings(fname,lname)
    surya.getSum()
    print(surya)

"""Now create user inputs. You can use the Modifer on demo
to add new data. You don't need to create a new object."""
main()
