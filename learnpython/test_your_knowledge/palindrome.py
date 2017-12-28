#! /usr/bin/python

# contact : sarath_v@icloud.com
#

from __future__ import print_function

my_string = raw_input("Enter your String \n")
try:
    my_string = basestring(my_string)

if my_string[:].upper().lower() == my_string[::-1].upper().lower():
    print('The given String is Palindrome')
else:
    print('The give String is NOT Palindrome')


