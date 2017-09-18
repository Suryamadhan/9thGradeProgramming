"""
Lab 19.1        Letter Remover
--------
In this lab you will write a program that removes an input letter from
a block of text. You will take user inputs for the text and for the
letter to be removed. The program will output the new text with the
letter removed.
"""

from LetterRemover import*

"""Test Cases"""
test = LetterRemover("I am Sam I am",'a')
print(test)
print(test.removeLetters() + "\n")

test.setRemover("ssssssssxssssesssssesss",'s');
print(test)
print(test.removeLetters() + "\n")

inpu = input(str("What is your string: "))
remove = input("What would you like to remove: ")
test.setRemover(inpu,remove)
print (test.removeLetters())
"""Take User Inputs"""

