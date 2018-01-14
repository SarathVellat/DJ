#! /usr/bin/python

# this is an example that shows usage of dictionary in python.
# dictionary works based on mapping. Each key is mapped to their values unlike we do indexing in list.


dict1 = {'key1':123,'key2':'hello world','key3':13.45}
print(dict1['key1'])
print(dict1.get('key1'))    # we can use .get method to get the value of  a particular key(it should not be vice versa)

#assigment of values.

dict1['key1'] = dict1['key1'] - 100
print(dict1['key1'])
dict1['key1'] -= 23
print(dict1['key1'])

#how to define a dictionary
new_dict = {}
new_dict['animal'] = 'tiger'
new_dict['answer'] = 123
print(new_dict)

new_dict1 = {'key1': 123,'key2':['item1','item2','item3'],'key3':13.45}
print(new_dict1['key2'][1])

#nesting dictionary

nest_dict = {'key1':{'key2':{'key3':'hello python'}}, 'key2':123}
print(nest_dict['key2'])
print(nest_dict['key1']['key2']['key3'])

#methods in dictionary
#this will never return the output in order.

print(new_dict1.keys())
print(new_dict1.values())
print(new_dict1.items())


