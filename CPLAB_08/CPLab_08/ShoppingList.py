"""
Ex_03
In this exercise, you will create a shopping list for
a party. You will list at least 4 items that you need
and print the results.
"""

class ShoppingList:
    def __init__(self, i1, i2, i3, i4):
        self.item1 = i1
        self.item2 = i2
        self.item3 = i3
        self.item4 = i4

    def getitem1(self):
        return self.item1
    def getitem2(self):
        return self.item2
    def getitem3(self):
        return self.item3
    def getitem(self):
        return self.item4

    def main():
        i1 = input("What is your item1?:  ")
        i2 = input("What is your item2?:  ")
        i3 = input("What is your item3?:  ")
        i4 = input("What is your item4?:  ")

        print ("1. item1 = ", i1)
        print ("2. item2 = ", i2)
        print ("3. item3 = ", i3)
        print ("4. item4 = ", i4)

    main()
