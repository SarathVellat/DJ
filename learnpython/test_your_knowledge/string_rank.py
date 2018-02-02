#! /usr/bin/python

from __future__ import print_function


a = {'A': 2, 'B': 2, 'C':3, 'D':4, 'E':10, 'F':6, 'G':8, 'H':9, 'I':20, 'J':11, 'K':12, 'L':13, 'M':14, 'N':15, 'O':32,
     'P':17, 'Q':18, 'R':19, 'S':20, 'T':21, 'U':44, 'V':23, 'W':24, 'X':25, 'Z':26}

s = raw_input('Enter your strings')
lst = list(map(str, s.split()))
new_dict = {}
lst_values= []

def caculator(lstt):
    sum=0
    for x in lstt:
        for letter in x.upper():
            sum=sum+(a.get(letter))
        new_dict[x] = sum
    for i in sorted(new_dict.values()):
        lst_values.append((new_dict.keys()[new_dict.values().index(i)]))
    print(lst_values[::-1])


caculator(lst)