#! /usr/bin/python

# contact : sarath_v@icloud.com
# This is python program that shows the usage of for loop.
# for loop act as an iterator. It goes through range, sequence or any other iterable item and execute the mentioned
# statements inside the loop.

from __future__ import print_function
from __future__ import division

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      # l is a list

for num in l:                            # the variable num doesnt need to be predefined here and it can be referenced
    print(num)                           # anywhere in the loop

# MODULO : % : This gives us the remainder value in a division

print(4%2)                               # returns
print(4%3)

# for loop to identify even and odd numbers

for num in l:
    if num % 2 == 0:
        print("%s is EVEN number" %(num))
    else:
        print("%s is ODD number" %(num))

# for loop to sum all the values of a given list

list_sum = 0                             # initializing a variable with 0 value

for sum in l:
    list_sum += sum

print("The sum of given list is %s" %(list_sum))

# for loop to print letters of a string

for letter in "Hello I am Sarath":
    print(letter)

# for loop to deal with tuple. Tuple is similar to list, but with immutability.

t = (1, 2, 3, 4)                        # t is a tuple

for num in t:
    print(num)

# Tuple Unpacking : When we use for loop to iterate through items that has tuples.

l = [(1,2), (3,4), (5,6)]

for tup in l:
    print(tup)

for (t1,t2) in l:
    print(t1)
    print(t2)

l1 = [(1,2,3), (4,5,6), (7,8,9)]

for (t1,t2,t3) in l1:
    print(t3)

# for loop to deal with Dictionary

d = {}
d['animal1'] = 'Lion'
d['animal2'] = 'Tiger'
d['animal3'] = "Deer"
d['animal4'] = 'Cat'
print(d)

for item in d:          # this way will print only the keys.
    print(item)

for item in d.iterkeys():
    print(item)

for item in d.itervalues():
    print(item)

for item in d.iteritems():
    print(item)

for k,v in d.iteritems():
    print(k)
    print(v)

# iteritems, iterkeys, itervalues -- basically these creates a generator that helps us to unpack items of a dictionary
# iteritems - came from iterator-generators 

# in python 3, this can be achieved through d.items()
# for k,v in d.items():
#   print(k)
#   print(v)

# generators don't store data in memory, but instead just yield it to you as it goes through an iterable item
# Python items() built a real list of tuples and returned that. That could potentially take a lot of extra memory.
