#! /usr/bin/python
# -*- coding: utf-8 -*-

"""This is an example that shows the usage of function.
contact : sarath_v@icloud.com

Function : Group of statements that can be run more than once. Also we can pass or specify parameters that can serve
as inputs to the functions
"""
from __future__ import print_function

def do_nothing():
    """
    This function does nothing when we call
    """
    pass

def hello_name(name):
    """
    :param name:
    :return: hello name
    """
    print("hello"+ name)

def my_addition(num1,num2):
    """
    :param num1:
    :param num2:
    :return: num1 + num2
    """
    add = num1 + num2
    print(add)

def my_difference(num1,num2):
    """
    :param num1:
    :param num2:
    :return: num1 - num2
    """
    return num1 - num2        # this will not print any output but gives a result that can then be stored as a variable,
                              # or used in whatever manner a user wants.


def is_prime(num):
    for n in range(2,num):
        if num % n == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

"""In the above function is_prime, along with the 'for' loop we also used 'else'. We can use 'else' in 'for' and 'while' 
loop, the else suite will be executed if we don’t exit the loop in any way other than its natural way which means if we 
stop the loop, say with a break statement, then the else suite will not be executed"""

# calling the above functons to see their results.
do_nothing()
hello_name('Sarath')
my_addition(5,6)
x = my_difference(6,5)
print(x)
is_prime(12)
