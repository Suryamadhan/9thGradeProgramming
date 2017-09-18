"""
* CPLab_14.2: 	    Triangle
* -----------
* In this lab you will create a loop that prints out
* a given word as many times as it has characters just
* like in Box, but with one character subtracted from
* the end each time the loop runs.
*
*
* input            output
* ------          -------
* hippo            hippo
*                  hipp
*                  hip
*                  hi
*                  h
-------------------------------------------------------"""

from TriangleOne import*

def main():
    """ Test cases - use these to make sure the
    object class works before going further."""
    #test = TriangleOne("hippo")
    #test.print()

    #test.setWord("chicken")
    #test.print()

    word1 = input("What is your word: ")
    surya = TriangleOne(word1)
    surya.print()

    """User Inputs:     <<<comment out the test cases>>>>
    * -------------
    * Create a Scanner input for the word, and use the
    * modifier on the "test" object to pass the new data
    * into test."""
main()
