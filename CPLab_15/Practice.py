__author__ = 'Surya'
def main():
    check = input("Please enter a String: ")

    count = 0
    for i in range(0, len(check)):
        if check[i] == "s":
            count+=1

    print("The String " + check + " contains ", count, " ss.")

main()

def contains13(num):
    return num % 13 == 0

def main():
    number = int(input("Please enter a number: "))

    count = 0
    for i in range(0, number):
        if contains13(i):
            count += 1

    print("The number ", number, " contains ", count, " 13s.")

main()