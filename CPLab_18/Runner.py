__author__ = 'Surya'
from AveragingDigits import*
def main():
    num = int(input("Enter a number :: "))
    average = AveragingDigits(num)
    print("The average of " + str(num) + " is......." + str(average.averageDigits()))
    print(average.sumDigits())

main()