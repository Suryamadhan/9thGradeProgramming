"""
* APLab _14.1:      Word Box
* ------------
* In this lab, you will create a "word box", where the loop
* prints the input word as many times as there are characters
* in the word. For example, the word "hippo" below has 5
* characters, and therefore would be printed 5 times.
*
* input            output
* ------          --------
* hippo            hippo
*                  hippo
*                  hippo
*                  hippo
*                  hippo
----------------------------------------------------"""

from Box import*

def main():
    """ Test cases - use these to make sure the
    object class works before going further."""
    test = Box("hippo")
    for i in range(len(test.getWord())-1,0,-1):
        print(test.getWord())
        i+=1
    test. __str__()
    print(test)

    #test.setWord("chicken")
    #print(test)

    word = input("What is your word: ")
    object = Box(word)
    for i in range(len(object.getWord())-1,0,-1):
        print(object.getWord())
        i+=1
    print(object.__str__())


    """User Inputs:     <<<comment out the test cases>>>>
    * -------------
    * Create a Scanner input for the word, and use the
    * modifier on the "test" object to pass the new data
    * into test."""
main()