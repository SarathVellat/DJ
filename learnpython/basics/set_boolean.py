#! /usr/bin/python

# This is a python program that shows the usage of SET and BOOLEAN in python

# Set is same as list with collection on UNIQUE items. Set doesn't has any items repeatedly in it.

x = set()                   # to define a set
print(x)

x.add(1)                    # we can add elements to set using set.add. We can add only one arguments at a time
print(x)
x.add(2)
print(x)
x.add(3)
x.add(4)
x.add(1.0)                  # even though we define element 1,it will not be getting added to the same set again
                            # thats the UNIQUE feature of set that differs it from list

l = [1,1,1,1,3,2,2,2,3]     # l is a list
print(l)
y = set(l)                  # casting of list type as set
print(y)


# Boolean. -- This holds the value True or False mainly. This also have a special place holder NONE

a = True        # Declaring variable as Boolean type by assigning either True, False or None
c = False
b = None

a = 1 > 2        # Since the variable is of Boolen type, we can equate our condition and if it pass then it prints True
print(a)         # else false.


c = 3 > 2
print(c)

b = 5 > 4
print(b)
