__author__ = 'Surya'
"""==============================================================
* Ex_04: Speaker Box
*
* Jimmy owns a stereo shop. There is a new subwoofer out
* that everyone wants, but it requires 3 cubic feet of space
* in order to run properly. Not many people have this much
* space to put a sub. Write a program to help Jimmy tell
* his customers whether or not he can install the sub.
============================================================"""

def main():
   l =int(input("What is the length: "))
   w =int(input("What is the weight: "))
   h =int(input("What is the height: "))

   calcVol(l,w,h)

def calcVol(l, w, h):

    minVol = 3
    maxVol = (l*w*h)*0.000578704

    if maxVol>= minVol:
        print("Yes, we can install it!!!")
    if maxVol < minVol:
        print("Sorry, no can do bro.")


main()