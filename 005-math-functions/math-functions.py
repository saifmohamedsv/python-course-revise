# Import the math module to use it's buil-in methods like ceil, floor ...etc
import math


pi = 3.14

# Round up/down the number to the nearest whole number, ex: 3.14 -> 3 / ex: 3.9 -> 4
print(round(pi))  # Built-In, don't need to import math module to use

# Ceil: always round the decimals UP to the nearest whole number.
print(math.ceil(pi))  # Output: 4

# Floor: always round DOWN the decimals to nearest whole number.
print(math.floor(pi))  # Output: 3

# Abs: tells you how far the number is away of zero also we can use it to switch from -ve to +ve numbers
print(abs(-3.14))  # Output: 3.14
print(abs(3.14))  # Output: 3.14

# Pow: raise the number to the power of n
print(pow(4, 2))  # Output: 16
# First argument is the number want to raise, second argument is the power

# Sqrt: Square root any number
print(math.sqrt(16))  # Output: 4.0

# Max: find the largest number among some numbers or in a given array
print(max([1, 2, 3]))  # Output: 3
print(max(1, 2, 3))  # Output: 3


# Max: find the smallest number among some numbers or in a given array
print(min([1, 2, 3]))  # Output: 1
