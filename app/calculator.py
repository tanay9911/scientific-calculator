import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if not isinstance(x, int):
        raise ValueError("Factorial requires an integer")
    if x == 0 or x == 1:
        return 1
    if x > 20:
        raise ValueError("Number too large for factorial calculation")
    
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def natural_log(x):
    if x <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers")
    return math.log(x)

def power(x, b):
    return math.pow(x, b)