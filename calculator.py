"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/SeagullBeagle/lab11-AS-NM
# Partner 1: Adam Siegel 
# Partner 2: Nicolas Murguia 

import math 

def square_root(a):
    if a < 0:
        raise ValueError("bad input")
    x = math.sqrt(a)
    return x

def hypotenuse(a, b):
    h = math.hypot(a, b)
    return h

def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b
    return c

def multiply(a, b):
    c = a * b
    return c

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("can't divide by 0")
    x = b / a
    return x

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("bad base")
    if b <= 0:
        raise ValueError("bad num")
    x = math.log(b, a)
    return x

def exponent(a, b):
    x = a ** b
    return x
    
    


