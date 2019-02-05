#!/usr/bin/env python3

import pyperclip
import re
import sys

# Raw String
print("This is a \n new line.")
print(r"This is not a \n new line.")

print("http:\newsite.com")
print("http:\\newsite.com")
print("http:\\\\newsite.com")
print(r"http:\\newsite.com")


# Join / Split
a = ['one', 'two', 'three']
b = ' '.join(a)
c = '<->'.join(a)
print('a =', a)
print('b =', b)
print('c =', c)

a = [1, 'two', 'three']
# b = ' '.join(a)         # TypeError: sequence item 0: expected str instance, int found

print('a b \nc  d'.split())             # ['a', 'b', 'c', 'd']
print('a b \nc  d'.split(' '))          # ['a', 'b', '\nc', '', 'd']
print('a b \nc  d'.split('\s+'))        # ['a b \nc  d']
print(re.split('\s+', 'a b \nc  d'))    # ['a', 'b', 'c', 'd']


# LJUST / RJUST / CENTER
print('hello'.ljust(20, '*'))
print('hello'.rjust(20, '-'))
print('hello'.center(20, '~'))


# Importing and using pyperclip
pyperclip.copy('Hello World')
a = pyperclip.paste()
print('a =', a)


# sys.argv
print(len(sys.argv))
print(sys.argv)
