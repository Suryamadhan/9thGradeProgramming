from BMI import*


def recalculate(n, h, w):

    choice = input("Would you like to recalculate: \t")
    if choice == "yes":
        main()
    else:
        print("Thank you for using Surya's BMI calculator! Have a good day")


def main():
    name = input("What is your name: ")
    height = int(input("What is your height in inches: "))
    weight = int(input("What is your weight in pounds: "))

    customer = BMI(name, height, weight)
    customer.calcBmi()
    print(customer)

    recalculate(name, height, weight)

main()