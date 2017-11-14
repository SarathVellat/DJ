#! /usr/bin/python

# This is an example showing how to use if_elif_else statements in python for different conditional checks.
# How it differs from other language is there is no usage of brackets or braces to define the conditional check blocks
# This use only colon and white space indentations.

# if case1:
#   perform action1
# elif case2:
#   perform action2
# else:
#   perform action3

from __future__ import print_function

# using boolean type here.

# example shows simple if statement
if True:
    print("The condition check was true")


# exmaple shows simple if else statements

x = False                               # boolean type

if x:
    print("The value of X is not true")
else:
    print("The value of X is true")

# exmaple shows simple if,elif and else statements

person = 'Sam'

if person == 'Sam':
    print("He is Sam")
elif person == 'Sammy':
    print("He is not Sam")
else:
    print("What's your name")

# Comparison Operators
# These operators will allow us to compare variables and output a Boolean value (True or False).
a = 1
b = 2
c = 2
d = 4

if c == b:
    print("Variables are equal")
elif b > a:
    print("B is greater than A")
elif b < d:
    print("B is smallert than D")
elif b >= c:
    print("B is greater than or equals to C")
elif b <> d:                                    # this is not supported in python 3.6, so use != instead
    print("B is not equal to D")
elif b != d:
    print("B is not equal to D")
else:
    print("End of the statements")

# Chain operators
# When we try to combine multiple relational operators to one

if 3 > 2 > 1:
    print("Condition is true")

# the above statement can be rewritten like this.

if 3 > 2 and 2 > 1:
    print("Condition is true here too")

if 1 < 3 > 2:
    print("Condition is true")

# the above statement can be rewritten like this.

if 1 < 3 and 2 > 1:
    print("Condition is true here too")

# using OR

if 1 == 1 or 100 == 1:
    print("Condition is True in one of the cases")
