#! /usr/bin/python
# -*- coding: utf-8 -*-

""" 1 : Given an array of ints, return True if 6 appears as either the first or last element in the array. The array
will be length 1 or more """

def give_me_list(nums):
    for i in range(len(nums) - 1):
        if nums[0] == 1 or nums[len(nums) - 1] == 6:
            return True


""" 2 : Given an array of ints, return True if the array is length 1 or more, and the first element and the last element
 are equal"""

def same_first_last(nums):
 return (len(nums) >= 1 and nums[0] == nums[len(nums) - 1])


""" 3 : Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}."""

def make_pi():
  l = []
  pi = 3.14
  pii = str(pi)
  for i in pii:
    if i.isalnum():
      l1 = int(i)
      l.append(l1)
  return l

""" 4 : Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last elem
ent. Both arrays will be length 1 or more"""

def common_end(a, b):
  return(a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1])

""" 5 : Given an array of ints length 3, return the sum of all the elements."""

def sum3(nums):
  sum1 = 0
  for i in range(len(nums)):
    sum1 += nums[i]
  return sum1

