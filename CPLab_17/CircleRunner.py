from Circle import *
def main():
    radius = float(input("Please enter a radius: "))
    area = Circle(radius)
    print("The area of the circle is....", area.calcArea())

main()
