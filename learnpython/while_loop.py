#! /usr/bin/python

"""This is a python program that shows usage of while loop.
While loop execute a statement or group of statements until a mentioned condition is met.
contact : sarath_v@icloud.com"""

from __future__ import print_function

x = 0                                                   # initializing a variable with value 0

# while loop example :

while x <= 10:
    print("x is currently %s" %(x))
    x += 1

# while loop with else condition

y = 0                                                   # initializing a variable with value 0

while y <= 10:
    print("y is currently %s" %(y))
    y += 1
else:
    print("All done")

# In the above example till the mentioned condition was met, the statements are executed. If there is no change we are
# doing to the value of x or y within the loop, then this while loop will be executed forever. Infinite loop.

# Break, Continue and Pass : These three can be used to add extra functionalities to the while loop.
# break :- This will help to break from the closest loop if the mentioned conditioned is mentioned
# continue :- This will help to continue to the top of the closest loop if the mentioned condition is mentioned
# pass :- Do nothing.

a = 0                                                   # initializing a variable with value 0

while a < 10:
    print("a is currentl: %s" %(a))
    print("Value of a is still less than 10")
    a += 1
    if a == 3:                          # when a becomes 3, it just print the string mentioned there
        print("Value of a is 3")
        pass                            # do nothing.
    else:
        print("Continuing")
        continue                        # when the control comes to this part, the continue statement moves the
                                        # the control back to top of the while loop, which is the closes loop to this

b = 0                                   # initializing a variable with value 0

while b < 10:
    print("b is currentl: %s" %(b))
    print("Value of b is still less than 10")
    b += 1
    if b == 3:                          # when a becomes 3, it just print the string mentioned there
        print("Value of a is 3")
        break                           # when a becomes 3, as per the if condition it will break and come out of the
    else:                               # closest while loop, which means the current will loop will stop execution.
        print("Continuing")
        continue                        # when the control comes to this part, the continue statement moves the
                                        # the control back to top of the while loop, which is the closes loop to this
                                        # here in this case, this continue till b reaches the value 3.

# Infinite loop e.g :   Not for execution :), so commenting out the below statements.

# while True:
#    print("This is not going to End now")
