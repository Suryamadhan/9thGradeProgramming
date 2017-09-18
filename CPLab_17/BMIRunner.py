from BMI import *
def main():
    height = int(input("Please enter height: "))
    weight = int(input("Please enter weight: "))
    
    bmi = BMI(height,weight)
    print(bmi.getBMI())
main()
