"""========================================================================================
* EX_01:           if-else statements
*
* Objectives:      The purpose of this lab is for you to demonstrate you have learned to use
*                  if-else statements to compare numerical data. You will be creating a
*                  program that returns the smallest and largest of two numbers.
*
* Instructions:    Use the existing test case below to test your NumberCompare class. Then
*                  create a new test class with user inputs for the numbers. Try out some
*                  different numbers to see how it works.
*
========================================================================================"""
import random
from NumberCompare import*
n1 = input("What is your first number: ")
n2 = input("What is your second number: ")
Surya = NumberCompare(n1, n2)
Surya = Surya.__str__()
print(Surya)

#now add a new test case with user inputs....

#Then test 3 more sets of numbers with the modifier