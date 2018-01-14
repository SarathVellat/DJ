#! /usr/bin/python

# this is python code example that shows the usage of tuple.
# tuples is also same as list in python but with a difference in feature called immuatability
# tuples is immutable because you cannot change the tuple items later once it is defined, where as in list you can
# reassign the lis item
# values. Also for tuples there are not many methods availables to use. Tuples can be used in python code when where we
# have to make sure
# the value are not changing. E.g : Calender

# how to declare a tuple

t = (1,2,3)
print(t)

t=('one',2,3.5)      # like list tuple can also have variety of data types in it.
print(t)

# indexing and slicing. This is simillar to what we do in list

print(t[-1])
print(t[1:])


# though a tuple is immutable, there are different ways using which we can change it value on a particular index.
# convert the tuple to a list, replace the element and convert back
lst = list(t)
lst[1] = '300'
t = tuple(lst)
print(t)

# Or we can do slicing

print(t)
t = t[:1] + (400,) + t[1:]
print(t)
t = t + (500,)                     # here if we just do +500  or +(500), it will give a type error. So we need to do
print(t)                           # + (500,) which means its tuple type.
