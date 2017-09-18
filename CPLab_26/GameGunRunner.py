"""import all from GameGun"""
from GameGun import *
def main():
    gun = GameGun()

    while gun.getBulletCount() > 0 or gun.getShotCount() > 0:
        action = input("Action: ")
        if action == "R" or action == "r":
            print(gun.reload())
        if action == "s" or action == "S":
            print(gun.shoot())

        print(gun)

    print("Out of bullets...")
main()

"""
=================================================================
new String action: set to ""
new GameGun() object called gun

while loop: runs as long as bulletCount and shotCount are > 0
    Take user input for action

    if action is R...
        reload your gun

    if action is S
        shoot your gun (print the result)

    print gun

print "Out of Bullets!!!"
===============================================================
"""