"""==============================================================================================
* Lab_10.3         The compareTo() method  (5 points)
*
* Objectives:      The purpose of this lab is for you to demonstrate you have learned to use
*                  if-else statements to compare String data with the compareTo() method.
*
* Instructions:    In this lab you will build a program that compares two words and tells you
*                  which one will come first and second in the Dicitonary.
*
================================================================================================="""
from WordsCompare import *
def main():
    name1 = input("What is the first word: ")
    name2 = input("What is your second word: ")

    Surya = WordsCompare(name1, name2)
    Surya = Surya.__str__()
    print(Surya)
main()
