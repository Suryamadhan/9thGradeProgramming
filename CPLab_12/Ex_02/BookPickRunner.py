"""==================================================================
Ex_02: Pick a Book

 You English teacher is conducting a timed reading. There
 are 3 books to choose from. You will create a program that
 allows you to pick a book from the available choices. Each
 potential choice is a "Book" object. Once you choose a book
 the program will print a passage from the book for you to
 read. 
 ===================================================================
 """
from Book import*

def bookChoice(mD, cR, gG):
    choice = input("Which book would you like to read?")
    if choice == mD.getName():
        choice = input("are you ready to read now?")
        if choice.upper() == "Y":
            print(mD)
        else:
            print("OK, but make sure you are finished by Friday!")
    else:
        print("You must have mispelled. Please try again")
        bookChoice(mD, cR, gG)

    if choice == cR.getName():
        choice = input("are you ready to read now?")
        if choice.upper() == "Y":
            print(cR)
        else:
            print("OK, but make sure you are finished by Friday!")
    else:
        print("You must have mispelled. Please try again")
        bookChoice(mD, cR, gG)

    if choice == gG.getName():
        choice = input("are you ready to read now?")
        if choice.upper() == "Y":
            print(gG)
        else:
            print("OK, but make sure you are finished by Friday!")
    else:
        print("You must have mispelled. Please try again")
        bookChoice(mD, cR, gG)

def main():
    mD = open("Moby Dick")
    cR = open("The Catcher in the Rye")
    gG = open("The Great Gatsby")

    mobyDick = Book("Moby Dick", mD.read())
    catcher = Book("Catcher in the Rye", cR.read())
    gatsby = Book("The Great Gatsby", gG.read())

    bookChoice(mobyDick, catcher, gatsby)
main()
    

