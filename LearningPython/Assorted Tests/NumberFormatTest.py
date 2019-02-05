
# String Modulo
n = 12345.67890
print(n)                        # 12345.6789
print('n = %8d' % n)            # n =    12345
print('n = %19.10f' % n)        # n =    12345.6789000000

n = 1
print('n = %f' % n)             # n = 1.000000
print('n = %05f' % n)           # n = 1.000000
print('n = %05d' % n)           # n = 00001
print('n = %.2f' % n)           # n = 1.00

# Multiple
a = 1
b = 12.34
print('a = %2d, b = %1.2f' % (a, b))    # a = 01, b = 12.34


# Format
n = 12345.67890
# print('n = {0:8d}'.format(n))   # ValueError: Unknown format code 'd' for object of type 'float'
print('n = {0:8f}'.format(n))   # n = 12345.678900
print('n = {0:19.10f}'.format(n)) # n =    12345.6789000000

n = 12345
print('n = {0:8d}'.format(n))   # n =    12345
print('n = {0:8f}'.format(n))   # n = 12345.000000
print('n = {0:08d}'.format(n))  # n = 00012345

a = 1
b = 12.34
print('a = {:3d}, b = {:5.2f}'.format(a, b))    # a =   1, b = 12.34
print('a = {0:3d}, b = {1:5.2f}'.format(a, b))  # a =   1, b = 12.34
print('a = {p:3d}, b = {q:5.2f}'.format(p=a, q=b))  # a =   1, b = 12.34
# print('a = {0:3d}, b = {1:d}'.format(a, b))  # ValueError: Unknown format code 'd' for object of type 'float'


# Line continuation
a = 1
b = 1
c = 3
x = a + \
    b + c
print(x)        # 5

