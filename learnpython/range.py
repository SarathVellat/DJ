#! /usr/bin/python

"""This is an example that shows usage range() function in python.
range allows us to create a list of numbers from a mentioned starting point to end point with a mentioned step size(
which is default by 1).
contact : sarath_v@icloud.com"""

from __future__ import print_function

print(range(0,10))                  # prints a list of value starting from 0 to 10
print(range(0,20,2))                # prints a list of value starting from 0 to 20, with a step size of 2, which means
                                    # all even number between 0 and 20

start = 0			    # default start is 0, so you can mention range(11) - 0 to 10
stop = 20                           # the list will contain values till stop, means excluding stop
step = 2

x = range(start,stop,step)          # intializing a variable with range
print(x)
print(type(x))                      # this will shows the type of the variable x, which will be list in this case

for num in range(0,10):             # range can be used in loop to iterate through required sequence
    print(num)

"""range() creates a list of values and it stores in the system memory. When it comes to large range of values like
1 to 10000000 etc, the memory usage matters and the execution of program may take a while to return the o/p.
So in python 2 it is recommended to use xrange() which is a generator that yeilds through the mentioned range and
returns the values, but it will never stores them in the memory"""

for num in xrange(0,10):
    print(num)

# The o/p looks same in both the cases, but xrange doesn't store the value in the memory

x = range(1,5)
x1 = xrange(1,5)

print(type(x))                  # list in this case
print(type(x1))                 # range in this cases, because the type of xrange is range

print(x1)                       # so the variable x1 will retrun the values xrange(1,5). Otherwise you have to use this
                                # in for loop to get the values

x1 = list(x1)                   # we can cast x1 as list and then get the values
print(x1)
