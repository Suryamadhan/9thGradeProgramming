from Question_1 import *
def main():
    height = int(input("Please enter the height of your cube: "))
    width = int(input("Please enter the width of your cube: "))
    depth = int(input("Please enter the depth of your cube: "))

    cube = Cube(height, width, depth)

    print(cube.getVolume())
main()