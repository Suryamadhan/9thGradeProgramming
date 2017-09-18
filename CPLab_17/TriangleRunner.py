from Triangle import *
def main():
    base = int(input("Please enter a base: "))
    height = int(input("Please enter a height: "))

    tri = Triangle(base, height)


    print(tri.getArea())
main()
