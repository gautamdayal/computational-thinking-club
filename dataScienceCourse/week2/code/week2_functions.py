"""
Functions
"""

# Defining a function

def double(a):
    return a * 2

# This function takes a given number and multiplies it by 2
# Here def is used to begin defining a function. The name of the function is kept as double, but can be whatever you want.
# The function takes one parameter, namely 'a', but functions can take multiple parameters and the name of the parameter can be whatever you like
# The statement 'return' followed by something gives back to the user the value of a * 2

print(double(5)) # So, if you were to run this, the output would be 10, and that would be printed on the screen.

def add(number1, number2):
    return number1 + number2

# This function takes two numbers and adds them and returns them to the user.

print(add(3, 5)) # So, if you were to run this, the output would be 8, since that is the sum of the two numbers, and that would be printed on the screen.

def hello():
    return "hello"

# Some functions can take no parameters at all. Looking at the function hello(), it does not take anything in, but still returns something, which is "hello"

print(hello()) # If this was run, the word "hello" would be printed on the screen, as the function returns hello to the user.
"""
Note: if a function returns a value, then the expression f(argument) where f is a function can be used as
if it were the output itself. For example, writing double(5) + 10 would be the same as writing 10 + 10.

Similarly, writing if a function isEven(n) returns a bool, writing if isEven(4): would be the same as writing
if True:
"""
