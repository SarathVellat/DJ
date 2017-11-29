#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
"""This is to show examples for using lambda expression in python.
contact : sarath_v@icloud.com

We use functions in python to avoid redundancy and to modularize the code(use the same set of block statements at many
place by calling this defined function). We can generally use two tools to create function in python 'def' and 'lambda'

lambda -- we use to create anonymous function where we doesnt define a name for it and generally use only once.
lambda funtions generally consist of expression that returns a value or evaluates, not statements. Since it has only
expressions it helps in squeezing the code. If the function needs to handle large and complex tasks then we need to use
'def' to create function.

"""

# example showing the usage of lambda.

def adder(num1,num2):                       # this is how we define a function using 'def'
    result = num1+num2
    return result

print(adder(1,2))

# the above function can also be rewrite like this to make it simple.

def adder1(num1,num2):
    return num1+num2

print(adder1(1,3))

# the above function can again rewrite like this to make it simple. This style of coding is not recommended because we
# always follow white space intendations.

def adder2(num1,num2): return num1+num2

print(adder2(1,5))

# so now we have seen a same function defined using 'def' in different ways to make our code simple and easy. The same
# thing can be replaced using lambda below.

adder_l = lambda num1,num2: num1+num2

print(adder_l(5,5))


# more examples

revstr = lambda str: str[::-1]                  # reversing a string

print(revstr('sarath'))

square = lambda num: num**2                     # square of a number

print(square(3))


even = lambda num: num % 2 == 0                # to check a given number is even or not. This returns boolean value

print(even(7))
print(even(8))


""" Difference between python statement and an expression : an expression returns (or evaluates to) a value, whereas a 
statement does not, but in Python an expression can also be a statement.

What kind of things can I, and can I not, put into a lambda ?

- If it doesn’t return a value, it isn’t an expression and can’t be put into a lambda.
- If you can imagine it in an assignment statement, on the right-hand side of the equals sign, it is an expression and 
  can be put into a lambda.
  
  
Why only one expression? Why not multiple expressions? Why not statements?: By the time that it was added, Python syntax
had become well established. Under the circumstances, the syntax for lambda had to be shoe-horned into the established 
Python syntax in a “pythonic” way. And that placed certain limitations on the kinds of things that could be done in 
lambdas.

Lambda is usually described as a tool for creating functions, but a lambda specification does not contain a return 
statement

Ref : https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/
"""