"""
Lab 19.2        Reverse Number
---------
In this lab, you will create a program that prints
out the reverse of the input number.

Sample Input        Sample Output
------------       ---------------
  5649               9465

"""

from ReverseNumber import*

"""Test Cases"""
test = ReverseNumber(84645)
print(test.__str__())


number = int(input("What is your number: "))
test.setNumber(number)
print(test.__str__())
"""Take User Inputs"""
