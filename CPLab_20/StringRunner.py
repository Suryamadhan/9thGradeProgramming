"""
Lab 20.2        First String
---------
In this lab, you will write a program that tells you
which of three Strings will come first in the dictionary.

"""

from FirstString import *
def main():

    """Test Cases"""
    run = FirstString("abc", "cba", "bca")
    print(run)
    print(run.getFirst(), " is the first.\n")

    run.setStrings("one", "fourteen", "twenty")
    print(run)
    print(run.getFirst(), " is the first.\n")

    """Create User Inputs...."""
    word1 = input("What is your first word: ")
    word2 = input("What is your second word: ")
    word3 = input("What is your third word: ")

    run.setStrings(word1,word2,word3)
    print(run)
    print(run.getFirst()+ " is the first.\n")
main()