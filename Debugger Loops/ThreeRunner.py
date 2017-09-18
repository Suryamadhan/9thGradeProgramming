"""Question 3: Division by Zero error.."""
from Three import *
number = int(input("Please enter a number: "))
factors = FactorCounter(number)
factors.countFactors()
print(factors)