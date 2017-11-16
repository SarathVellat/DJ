#! /usr/bin/python

# This is an example that shows basic usage of list in python.

from __future__ import print_function

my_list1 = [1,2,3]
print(my_list1)

# difference of list from array is,it can have objects of different data types..
#.. and there is no constrain of definite size.

my_list2 = [1, 'hello', (13.45)]
print(my_list2)
print(my_list2*2)                           #arithmetic expressions * can be used for printing the string multiple times

# list indexing and slicing

print(my_list1[1])
print(my_list2[1:])
print(my_list1[:1])
print(my_list1[-1])
print[my_list1[::-1]]

# list properties

my_list1 = my_list1 + ['add me']             #concatenation
print(my_list1)

my_list2.append('add me at the end')         #appending -- this change is permanent to the list
print(my_list2)

my_list2.pop()                               # pop by default this will slice the last index and this change is permanent to the list
print(my_list2)
print(my_list2.pop())
print(my_list2)

my_list3 = [1, 'apple', 'orange', 13.45, 3, 'a']
print(my_list3)
print(my_list3.pop(2))
print(my_list3)

print(my_list3.reverse())
print(my_list3)
print(my_list3.sort())
print(my_list3)

#nesting lists

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]

matrix = [list_1,list_2,list_3]

# list comprehension

print(matrix)
print(matrix[1][1])
new_list = [row[0] for row in matrix]
print(new_list)
