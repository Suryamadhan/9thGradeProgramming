__author__ = 'Surya'
from GetSs import*

def main():
    check = input("Please enter a String: ")
    s = GetSs(check)
    print(s)

    check = input("Please enter another String: ")
    s.setCheck(check)
    print(s)


main()