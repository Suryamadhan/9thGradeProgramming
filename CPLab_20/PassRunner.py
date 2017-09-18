"""
Lab 20.3          Password Check
---------
In this exercise, you will create a password program
that congratulates you when you "hack" it's password.
The program will continue to ask for a password until
you enter the correct one.
"""

from PasswordCheck import *
"""
This method just runs the program. It just runs the
object class. You will not need to add user inputs or
alter it in any way.
"""
def main():
    test = PasswordCheck()
    test.check()

main()