#! /usr/bin/python

# This is a python program that shows how to deal with files in our computer.
# For Special files like audio files etc, we may need to have extra modules imported.

f = open('test.txt')        #open a file
print(f.read())             # to read the content of the file and print it
f.seek(0)                   # f.read first time read the content and now it is at the end of the file. I is same as the
                            # curson. So using f.seek(0) we are resetting the cursor starting point to beginning of the
                            # file.
print(f.read())


for line in open('test.txt'):
    print line


# more features yet to come.... :)
