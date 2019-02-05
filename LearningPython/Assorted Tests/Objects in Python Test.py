# The bool Class
print(bool())           # False
print(bool(False))      # False
print(bool(True))       # True
print(bool('False'))    # True   //as length of 'False' is more than 0
print(bool('false'))    # True
print(bool(0))          # False  //as the numerical value is 0
print(bool(-1))         # True   //as the numerical value is not 0
print(bool(1))          # True   //as the numerical value is not 0
print(bool(0.0))        # False  //as the numerical value is 0
print(bool(0.1))        # True   //as the numerical value is not 0
print(bool(''))         # False  //as length of '' is 0
print(bool('abc'))      # True   //as length of 'abc' is more than 0
print(bool([]))         # False  //as length of [] is 0
print(bool([1, 2]))     # True   //as length of [1, 2] is more than 0

# The int Class
print(int())            # 0
print(int(1))           # 1
print(int(3.14))        # 3
print(int(3.99))        # 3
print(int(-3.14))       # -3
print(int(-3.99))       # -3
print(int('1'))         # 1
# print(int('3.14'))    # ValueError: invalid literal for int() with base 10: '3.14'
print(int(' 1 '))       # 1
# print(int(' 1 2 '))   # ValueError: invalid literal for int() with base 10: ' 1 2 '
print(int(' 12 '))      # 12
# print(int(' 3 . 1 4'))# ValueError: invalid literal for int() with base 10: ' 3 . 1 4'
# print(int('12ab'))    # ValueError: invalid literal for int() with base 10: '12ab'
# print(int('ab12'))    # ValueError: invalid literal for int() with base 10: 'ab12'
print(int(0b101))       # 5
# print(int('0b101'))   # ValueError: invalid literal for int() with base 10: '0b101'
print(int(0o11))        # 9
print(int(0xa1))        # 161
print(int(0xA1))        # 161
print(int('00101', 2))  # 5
print(int('a1', 16))    # 161
print(int('z1', 36))    # 1261
# print(int('a1', 8))   # ValueError: invalid literal for int() with base 8: 'a1'
print(int(1e2))         # 100
print(int(1e-2))        # 0
# print(int('1e2'))     # ValueError: invalid literal for int() with base 10: '1e2'
# print(int('1e-2'))    # ValueError: invalid literal for int() with base 10: '1e-2'

# The float Class
f = 2.0
print(type(f))          # <class 'float'>
f = 2.
print(type(f))          # <class 'float'>
f = 2
print(type(f))          # <class 'int'>
print(float(2))         # 2.0
print(float('2'))       # 2.0
print(float('2.000'))   # 2.0
print(float(' 2.0 '))   # 2.0
# print(float(' 2 . 0 '))# ValueError: could not convert string to float: ' 2 . 0 '
print(float(1e-2))      # 0.01
print(float(1e2))       # 100.0
print(float('1e-2'))    # 0.01
print(float(' 1e-2 '))  # 0.01
# print(float(' 1 e-2 '))# ValueError: could not convert string to float: ' 1 e-2 '
print(float('1e2'))     # 100.0


