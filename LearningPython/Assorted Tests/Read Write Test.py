import os

# Read
name = 'Read Write Test.py'
f = open(name, 'r')
s = f.read()
print(s)

f = open(name, 'r')
s = f.readlines()
print(s)

name = 'anyfile.txt'
# f = open(name)  # FileNotFoundError: [Errno 2] No such file or directory: 'anyfile'


# Write
s = """Line1
Line2
Line3
"""
name = 'anyfile.txt'
f = open(name, 'w')
f.write(s)
f.write('End of lines.')
f.write('Last lines.')
f.close()

f = open(name, 'r')
print(f.read())
