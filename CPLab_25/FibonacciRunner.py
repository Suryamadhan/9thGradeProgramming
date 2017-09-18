"""===============================================================
Lab_24.1        Fibonacci Sequence
---------
 * In this lab, you will generate a Fibonacci sequence.
 * Each number in a Fibonacci sequence is the sum of the
 * two preceding numbers in the sequence. The first two
 * numbers are naturally always both 1. The third, fourth,
 * fifth, and sixth numbers are 2, 3, 5, and 8 respectively.
 *
 * The getFibo() method should return the number at a specified
 * index in the sequence. For instance, getFibo(8) should
 * return 21, which is the 8th number in the sequence.
================================================================"""
from Fibonacci import *

"""Fibonacci Object..."""
fib = Fibonacci(50)
print(fib)

"""Test Cases..."""
print(fib.getFibo(1))
print(fib.getFibo(2))
print(fib.getFibo(3))
print(fib.getFibo(4))
print(fib.getFibo(5))
print(fib.getFibo(6))
print(fib.getFibo(11))
print(fib.getFibo(16))
print(fib.getFibo(21))
print(fib.getFibo(31))
print(fib.getFibo(41))
print(fib.getFibo(46))

"""
User Inputs...
Use the modifier to take user inputs for index size
"""
inputs = int(input("Till what number do you want your Fibonacci sequence to be: ")) +1
fib = Fibonacci(inputs)
print(fib)

"""
Take user inputs for getFibo()
Get this fibo number at the specified index
"""