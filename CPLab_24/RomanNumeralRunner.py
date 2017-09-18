"""
==================================================================
Lab_24.1        Roman Numeral Converter
---------
In this lab, you will write a program that takes user inputs
for Roman Numerals or Decimal Numbers. If user inputs a Decimal
Number, the program converts it to Roman Numerals. If user inputs
a Number in Roman Numerals, the program converts it to a Decimal
Number
====================================================================
"""

from RomanNumeral import *
""" Test Cases..."""
test = RomanNumeral("", 10)
print(test)

test = RomanNumeral("LXXVII", 0)
print(test)

"""
Add user inputs...
Hint: ask user if they want to convert decimal --> roman
or roman --> decimal. You need an if statement to know
where to put your input.
"""
print("Welcome to Roman numeral converter.")
print("What do you want do: ")
print("1. Convert Roman into Number")
print("2. Convert number into Roman")
want = input("")
if want == "1":
    wants = input("What is your roman character: ")
    wants = wants.upper()
    test = RomanNumeral(str(wants), 0)
    print(test)
if want == "2":
    wants = int(input("What is your number: "))
    test = RomanNumeral("", wants)
    print(test)
