"""================================================================
    * Lab_13.3
    *
    * Lab Goal :
    * -----------
    * This lab was designed to teach you more about objects and
    * the String class.
        *
    * Lab Description :
    * -----------------
    * One person is going to marry another person and take his or
    * her last name. You will write a program that allows you to
    * enter the full name of the person getting married, and his or
    * her potential spouse, and return the full name of the person
    * getting married, including his or her new last name.
    *
    *
    * Sample Data :        Sample Output :
    * ------------         ---------------
    * Sally Baker          If Sally Baker marries Arnold Palmer.....
    * Arnold Palmer        Sally's name wil be Sally Palmer
    *
==================================================================="""

from Marriage import*

def main():

    """Test Cases"""

    spouse1 = "Sally Baker"
    spouse2 = "Arnold Palmer"


    marry = Marriage(spouse1, spouse2)

    print(marry)

    newspouse1 = input("Who is your spouse 1(this is the girl who is getting married: ")
    newspouse2 = input("Who is your spouse 2(this is the boy who is getting married: ")

    object = Marriage(newspouse1,newspouse2)
    print(object)

    """Now take user input for spouse1 and spouse2. You should know by
    * now that you don't need to make another Marriage object. Use the
    * modifier in marry to add new data
    *
    * 1. Add new Scanner object
    * 2. Add user inputs for spouse1 and spouse2
    * 3. Place input data into the modifier
    * 4. print the object's toString()"""



main()
