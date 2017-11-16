#! /usr/bin/python

# this is python program that shows how to deal with numbers in python.
# contact : sarath_v@icloud.com

# using the feature __future__ we are importing the division operation from python 3 so that it will perform classic division.

from __future__ import division

#variable assignment
a = 10
b = 3
x = 0.1
y = 0.2
z = 0.3
q = -3
#arithmetic operations addition, subtraction, multiplication

sum = a + b
diff = a - b
mul = a * b


#normal divison in python 2 will not do classic division

div_normal = a/b

#casting a variable as float so that the division also give float result -- classid division
div_casting = float (a)/b
power = a**b

print ("Addition result is %s:") %sum
print ("Subtraction result is %s:") %diff
print ("Multiplication result is %s:") %mul
print ("Normal division result is %s:") %div_normal
print ("Float division result is %s:") %div_casting
print ("Power result is %s:") %power

#arithmetic operation in python follows the rule BODMAS , not with order they are given in the arithmetic experssion
test1 = 10 * 3 + 10 * 3
test2 = (10 * 3) + (10 + 3)
test3 = x + y - z

print ("Test1 is an example shows the arithmetic expression doesn't follow the order %s:") %test1
print ("Test2 is an example shows the arithmetic expression follow the rule BODMAS %s:") %test2
print ("Test3 is an example that shows non zero result because of floating point accuracy and computer ability to represent number in memory:%s") %test3

#Advanced features that can be used in Python for dealing with numbers

binary_value = bin(a)
hexa_value  = hex(a)
power_value = pow(a,b)
absolute_value = abs(q)
round_value = round(div_casting, 1)      #by defaul it round to zero digits


print ('Binary value of variable a is %s') %(binary_value)
print ("Hexa value of variable a is %s") %(hexa_value)
print ("a to the power of b is %s") %(power_value)
print ("Absolute value of variable q is %s") %(absolute_value)
print ("Round value of after classic division is %s") %(round_value)
