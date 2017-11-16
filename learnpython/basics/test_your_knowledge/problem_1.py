#! /usr/bin/python
# -*- coding: utf-8 -*-

# above line is for source code encoding.

"""Problem no : 1 : Use for,split(), and if to create a Statment that will print out letters that start with 's':"""


st = 'Print only the word that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(word)
    else:
        continue


"""Problem no : 2 : Use range() to print even numbers from 0 to 10."""

for num in range(0,11):
    if num % 2 == 0:
        print num
    else:
        continue

"""Problem no : 3 : Use list comprehension to create a list of all numbers between 1 to 50 that are divisible by 3"""

lst = [x for x in xrange(1,51) if x % 3 == 0]
print(list(lst))                        # since we are using xrange, the type will be xrange for lst, so we are casting
                                        # lst as list type to return the values.

"""Problem no : 4 : Use list comprehension to convert celsius reading to Fahrenheit"""

# T(°F) = T(°C) × 9/5 + 32 - formula needs to be used for this conversion

celsius = [0, 1, 5, 90, 102.5]          # list temp values in Celsius

fahrenheit = [(temp * 9/5 +32) for temp in celsius]
print(fahrenheit)

"""Problem no : 5 : Go through the string below and if the length of a word is even print 'even'."""

st = 'Print only the word that start with s in this sentence'

length = len(st)
if length % 2 == 0:
    print("Even")

"""Problem no : 6 : Write a program that print integers from 1 to 100, But for multiples of three print 'Fizz' instead 
of the numberand for the multiples of five print 'Buzz'. For numbers which are multiplies of both 3 and 5 print 
'FizzBuzz'"""

for num in xrange(101):
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        if num % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(num)

# the above code can also be rewritten like

for num in xrange(101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

"""Problem no : 7 : Use list comprehension to create a list of the first letters of every word in the string below: """

stt = 'Create a list  of the first letters of every word in this string'

lst = [word[0] for word in stt.split()]
print(lst)


"""Source code encoding :
Python 2 will default to ASCII as standard encoding if no other encoding hints are given. Python 3 use utf-8 by default.
To define a source code encoding, a magic comment must be placed into the source files either as first or second line in
the file, such as:
     # coding=<encoding name>

or (using formats recognized by popular editors)

      #!/usr/bin/python
      # -*- coding: <encoding name> -*-
or
      #!/usr/bin/python
      # vim: set fileencoding=<encoding name> :
      
In this program # T(°F) = T(°C) × 9/5 + 32 - formula needs to be used for this conversion --this has non-ASCII character

Refer : https://gist.github.com/gornostal/1f123aaf838506038710
"""
