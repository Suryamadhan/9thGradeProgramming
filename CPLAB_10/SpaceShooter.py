import random

target = int(input("Enter your target: "))
enemyLoc = random.randint(1, 7)

if target == enemyLoc:
    print("It's a hit!")

else: #in all other cases
    print("Keep Trying! The universe depends on you!")



