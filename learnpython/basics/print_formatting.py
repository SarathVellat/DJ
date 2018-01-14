#! /usr/bin/python


# This is a python program that shows different types of formatting we can have using print statement (or print function in python 3)

# in python 2, print is a statement where as in python 3 it is a function.
# print 'Your string' -- this print the Your string in python 2 where print is a statement.
# print ('Your string') -- this print the Your string in python 3 where print is a function.
# using future feature we are importing the print_function from python 3 to python 2


from __future__ import print_function


# how to pass a variable value to the print function

x = 'String'

print('Place my variable here %s' %(x))

# type conversion in print formatting.

y = 123

print('Type conversion here. Inteeger value of y is now printed as a string : %s' %(y))   # %s uses the function string
print('Type conversion here. Inteeger value of y is now printed as a string : %r' %(y))   # %r uses the function repr


f = 13.145

#%1.2f : 1 - indicates minimum number of value that should be there before decimal. If its more than what is present then it will be filled
# with white spaces..2f - indicates the number of values after decimal. If its more than what is available then it will be filled with
# zeroes

print('The float value of variable f is : %1.2f' %(f))
print('The float value of variable f is : %10.2f' %(f))
print('The float value of variable f is : %1.10f' %(f))
print('The float value of variable f is : %1.2f' %(13.145))

#print formatting by passing multiple variable value.

a=1
b=2
c=3
print('First : %s, Second : %s, Third : %s' %(1,2,3))
print('First : %s, Second : %s, Third : %s' %(a,b,c))

#we can use .format method in print formatting to avoid passing variable values multiple times.

print('First : {z}' .format(z="inserted"))
print('First : {x}, Second : {y}, Third : {x}' .format(x=1,y=2))
print('First : {g}, Second : {z}' .format(g="hello",z="inserted"))

print("The value of a is : {0}, the value of b is: {1}, the value of c is: {2}".format(a,b,c))

print("The first value is: {e}, the second value is: {f} and the third value is: {g}".format(e='2', f='3', g='4'))

