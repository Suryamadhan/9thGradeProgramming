"""=================================================================
* Ex_01: Discount
* Alfred is having a sale at his tire shop. Customers who spend
* $2000 or more will receive a 15% discount. Write a program for
    * Alfred's POS system that enters the discount automatically.
================================================================"""


def main():
    """Inputs for cost1, 2, 3"""
    cost1 = int(input("Enter the value of item1: "))
    cost2 = int(input("Enter the value of item2: "))
    cost3 = int(input("Enter the value of item3: "))
    cost4 = int(input("Enter the value of item4: "))

    """Calculate Subtotal"""
    subTotal = cost1+cost2+cost3+cost4

    """Conditional Logic:
    if subTotal > 2000
        give 15% discount
        print total """

    """if subTotal <= 2000
        print no discount
        print subTotal"""
    if subTotal > 2000:
        total = subTotal*0.85
        print ("You got 15% off!")
        print ("Total: ", total)
    if subTotal <= 2000:
        print("No discount for you")
        print("Total: ", subTotal)

main()