from SlotMachine import *
"""
    EX_03: Slot Machines
    Define a main() method:
        Create 8 SlotMachine objects with names
        Run each of their hitJackPot() functions
        print each of the SlotMachine objects using __str__()
"""
def main():
    M1 = Slotmachine("Jack")
    M2 = Slotmachine("John")
    M3 = Slotmachine("Zack")
    M4 = Slotmachine("Jimmy")
    M5 = Slotmachine("Russel")
    M6 = Slotmachine("Harry")
    M7 = Slotmachine("Percy")
    M8 = Slotmachine("Justin")
    M9 = Slotmachine("Nick")
    M10 = Slotmachine("Armstrong")

    M1.hitJackpot()
    print(M1.__str__())
    M2.hitJackpot()
    print(M2.__str__())
    M3.hitJackpot()
    print(M3.__str__())
    M4.hitJackpot()
    print(M4.__str__())
    M5.hitJackpot()
    print(M5.__str__())
    M6.hitJackpot()
    print(M6.__str__())
    M7.hitJackpot()
    print(M7.__str__())
    M8.hitJackpot()
    print(M8.__str__())
    M9.hitJackpot()
    print(M9.__str__())
    M10.hitJackpot()
    print(M10.__str__())





main()