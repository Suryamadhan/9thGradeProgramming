"""Ex_03: Adventure

 Copy and paste the Adventure program from Lesson_10
 into this file Follow along with the tutorials and
 finish the Adventure exercise. Be sure to follow the
 original directions.
"""
choice = int(input("After you go to your basketball practice what do you do?\n"
                   "1. Socialize yourself with your friends\n"
                   "2. Start practicing with you coach.\n"
                   "Which Choice: "))
if choice ==1:
    choice = int(input("What do you do while talking with your friends?\n"
                    "1. Play Basketball while talking to your friends.\n"
                    "2. Just Stand out there and talk\n"
                    "Which Choice: "))
    if choice == 1:
        choice = int(input("How do you play while doing this\n"
                     "1. Play hard\n"
                     "2. Barely Play\n "
                     "Which choice: "))
        if choice == 1:
            print ("You are socializing yourself, and at the same time getting those calories burn. Nice job!")
        else:
            print ("Just try playing hard man. You will burn those calories")
    else:
        print ("MAn.., You need to get involved in the game.")
else:
 print("Its all about socializing yourself man...")
