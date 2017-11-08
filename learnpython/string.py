#! /usr/bin/python

# this is a python program how to deal with Strings in python.
# contact : sarath_v@icloud.com

# in python 2, print is a statement where as in python 3 it is a function.
# print 'Your string' -- this print the Your string in python 2 where print is a statement.
# print ('Your string') -- this print the Your string in python 3 where print is a function.
# using future feature we are importing the print_function from python 3 to python 2

from __future__ import print_function

# we can use single or double quotes to print a string in python like given below.We use double quotes in cases where the sting itself..
# ..has single quote to print.
# in python every letters in a string is printed with respect to their sequence including the blank space.

print ('Hello World')
print ("Hello I'm Sarath Vellat")

# below examples shows how to use different escape sequence to go to new line, how to enter a tab between stings etc.

print ('This is first line \nThis is second line')
print ('This is first line \tThis is second line')

# String Basics

s='hello World'
print(s)

length=len('s')            #to get the lenght of a string. This count the white spaces too between the letters
print(length)

#String indexing

print(s[1])                # indexing starts from 0. 0 index point to the first letter of the string
print(s[-1])               # reverse indexing, which starts with negative 1

#String slicing

print(s[:])                # this print the whole string because this inidicates from the beginning to the end of the string
print(s[1:])               # this means from the index 1 onwards till the end
print(s[:4])               # This means from the beginning upto index 4 -- excluding 4
print(s[1:4])              # this means from index 1 onwards upton index 4 -- that means excluding 4
print(s[:-1])
print(s[::1])              # this shows String slicing with step size one. first two represent from the beginning to end and third value shows the steps size
print(s[::2])
print(s[::-1])             # this is for reversing a given string

#String Properties

# immutability : This means we cannot change the value of any index of a string. String in python is considered in the form of a sequence..
#.. and thus its not possible to change the value of any index later. For e.g : s[1] = G , will error out

length = 'z'
print(length)
print(length*10)           # we can use arithmetic expression * to print a string multiple times
print(s)
a = s + " concatenate me"  # to join two strings
print(a)
print(s)
print(s.upper())           # comes under String properties for lower and upper case conversion
print(s.lower())
print(s.split())           # for Splitting - by default it goes with white spaces.
print(s.split('o'))


#Advance features in python to deal with Strings.

print(s.capitalize())      # capitalize -- make the first letter of the string as captital
print(s.count('o'))        # count the occurence of a specified letter
print(s.find('o'))         # find the index where the specified letter is present in a string
print(s.find('l',3))       # find the index where the specified letter is present in a string between the mentioned start and end index.
print(s.center(20,'*'))    # ceneter the string between the mentioned letter and make the whole output string of mentioned length.

#is check methods
print(s.isalpha())  # True if all characters in the string are alphabetic and atlest one character. No digits and space
print(s.isalnum())  # True if all characters are either alphabetic or numerical and atlest one character.. No space.
print(s.islower())  # True if all characters are lower case and atlest one character.
print(s.isupper())  # True if all characters are upper case and atlest one character.
print(s.isspace())  # True if all character in the string is whitespace.
