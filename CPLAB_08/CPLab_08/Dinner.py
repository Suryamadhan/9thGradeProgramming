"""
Ex_01

In this exercise, you will be putting together a dinner plate. You
will create inputs for the meat, vegetable, starch, appetizer, and
drink, and print out your dinner at the end.
"""

class Dinner:
    def __init__(self, m, v, s, a, d):
        self.meat = m
        self.vegetable = v
        self.starch = s
        self.appetizer = a
        self.drink = d

    def getMeat(self):
        return self.meat
    def getVegetable(self):
        return self.vegetable
    def getStarch(self):
        return self.starch
    def getAppetizer(self):
        return self.appetizer
    def getDrink(self):
        return self.drink

    def main():
        m = input("What meat are you consuming today? ")
        v = input("What vegetable are you going to eat today? ")
        s = input("What source of starch are you consuming today?  ")
        a = input("What appetizer are you going to eat today? ")
        d = input("What drink are you going to drink today? ")

        print ("Meat:     ", m)
        print ("Vegetable:", v)
        print ("Starch:   ", s)
        print ("Appetizer:", a)
        print ("Drink:    ", d)

    main()
    """Constructor: inputs for meat, veg, starch, appetizer, and drink"""


    """Modifier: reset your food items on each object"""

    """Accessors: one for each of the food items"""


"""
    Main function
    take user inputs, instantiate a new Dinner object, and
    print out your dinner. You should get results similar to
    the following....

    Your dinner tonight....
    Meat:		 Ribeye
    Vegetable:	 Peppers
    Starch:		 Baked Potatoes
    Appetizer:	 Mozzarella Sticks
    Drink:		 Coke
"""
