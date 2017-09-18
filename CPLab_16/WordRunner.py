"""
* APLab_16.1:    WordRunner
* -----------
* This lab should be review for you. You will create
* a program that allows you to enter a word, and then
* prints the first character, the last character, and
* then the word itself backward.
"""

from Word import *

def main():
    word = input("What is your word: ")
    surya = Word(word)
    surya = surya.__str__()
    print(surya)



    """Now take user inputs......"""

main()
