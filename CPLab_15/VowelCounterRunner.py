"""
* CPLab_15.3: 		Vowel Counter
*------------
* In this lab, you will create a program that will count the
* vowels in any String. You will take a String input and
* output the number of vowels in that String
*
* Sample Input         Sample Output
*--------------       ---------------
* qwertasdyuio              5
*
* --------------------------------------------------------"""


from VowelCounter import*
def main():
    String = input("What is your word or whatever you want to call it: ")
    Surya = VowelCounter(String)
    print(Surya)
main()
"""Now comment out everything in the test cases except the new
* object, and create user input for the Strings. Add the new
* String values to the modifier (parameters) and print test again."""