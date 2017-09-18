""" ===========================================================
* EX_02: Odd or Even?
*
* Create a program that allows the user to input a number,
* then tells the user whether the number is even or odd.
=========================================================== """
def oddeven():
    number = int(input("What is your number: "))
    if number % 2 == 0:
        print("Yor number is even.")
    if number % 2 == 1:
        print("Your number is odd.")

oddeven()
