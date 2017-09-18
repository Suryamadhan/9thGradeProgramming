"""
Lab 19.3        Perfect
---------
In this lab, you will right a program that checks to see if an
input number is "perfect". A perfect number is one whose divisors
add up to the number itself.

Sample Input            Sample Output
-------------          ---------------
  496                   496 is perfect
  1245                  1245 is not perfect
"""

from Perfect import *

"""Test Cases...."""
test = Perfect(496)
print(test)

test.setNum(1245)
print(test)

number  = int(input("What is your number: "))
test.setNum(number)
print(test)

"""Take User Inputs...."""