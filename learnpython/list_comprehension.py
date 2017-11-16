#! /usr/bin/python

"""This is an example that shows usage of list comprehension in python
list hold values, and using list comprehension we can build using different notations or one for loop inside the
bracket
contact : sarath_v@icloud.com"""

lst = [1,2,3,4,5]                               # a normal list

lst1 = [letter for letter in "word"]            # simple list comprehension

print(lst1)

"""In the above example, we are defining the required object 'letter' and then assinging the value to it from the 
string. The same example can be rewritten using normal for loop"""

lst2 = []                                       # defining a list

for letter in "wording":
    lst2.append(letter)

print(lst2)

# more examples :

lst3 = [x**2 for x in range(11)]            # defined the list object as x**2, so that for each value of x in the
print(lst3)                                 # range(11), it square the value and store it in the list

lst4 = [y**2 for y in xrange(11)]           # same as above but we use xrange to minimize the usage of memory in python2
print(lst4)

# nested list comprehension

lst5 = [z**2 for z in [y**2 for y in xrange(11)]]
print(lst5)

"""The above example shows nested list comprehension, where the list object defined as z**2 which inturn takes the 
value from the list which has the object defined as y**2 so that fo each value of y in the range(11), it squares the
value and assign to z. So the final result is acutally referring to z**4 for the each value of z in the range(11)"""
