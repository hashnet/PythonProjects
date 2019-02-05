import copy

# List
a = [1, 2, 3]
print('a =', a)
a = ['a', "b", 1]
print('a =', a)
a = list('abc')
print('a =', a)


# Tuple
a = 1, 2, 3
print('a =', a)
a = (1, 2, 3)
print('a =', a)
a = tuple('abc')
print(a)
a = 1,
print(a)


# Array like indexing
print([1, 2, 3][0])     # for list
# print([1, 2][10])     # IndexError: list index out of range
print((1, 2, 3)[0])     # for tuple
# print((1, 2, 3)[10])  # IndexError: tuple index out of range


# Multidimensional
a = [[1, 2, 3], ['a', 'b'], [10, "p", 10.2, [100, 200]]]
print(a[0])
print(a[2])
print(a[0][1])
print(a[1][1])
print(a[2][2])
print(a[2][3])
print((a[2][3])[0])
print(a[2][3][0])


# Negative index
print([1, 2, 3][-1])
print([1, 2, 3][-3])
# print([1, 2, 3][-4])    # IndexError: list index out of range


# Sublit with slices
print([0, 1, 2, 3][1:3])
print([0, 1, 2, 3][1:300])
print([0, 1, 2, 3][100:300])
print([0, 1, 2, 3][-3:-1])
print([0, 1, 2, 3][-3:0])

print([0, 1, 2, 3][:2])
print([0, 1, 2, 3][2:])


# Concatenate
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(a + b)
print(b + a)
# print(a + 4)        # TypeError: can only concatenate list (not "int") to list
print(a + [4])

print([1]*4)
print([0, 1]*4)


# Deleting item
a = [1, 2, 3]
del a[1]
print('a =', a)
# del a[2]            # IndexError: list assignment index out of range

a = [1, 2, 3]
a.remove(1)
print('a =', a)
# a.remove(10)        # ValueError: list.remove(x): x not in list

# For loop with list
a = [0, 1, 2]
index = 0
for i in a:
    print('a[' + str(index) + '] = ' + str(i))

a = ['a', 'b', 'c']
index = 0
for i in a:
    print('a[' + str(index) + '] = ' + i)

a = ['a', 'b', 'c']
for i in range(len(a)):
    print('a[' + str(i) + '] = ' + a[i])

# In Check
a = [1, 2, 'a', 'b']

print(1 in a)
print(10 in a)
print('a' in a)
print('aa' in a)
print('aa' not in a)
print('b' not in a)


# Multi Assignment
a = [1, 2, 'a']
x, y, z = a
print(x)
print(y)
print(z)

# x, y, z, n = a      # ValueError: not enough values to unpack (expected 4, got 3)
# x, y = a            # ValueError: too many values to unpack (expected 2)


# Index / Append / Insert
a = [1, 2, 3]
print(a.index(3))
# print(a.index(4))   # ValueError: 4 is not in list

a.append('a')
print('a =', a)

a.insert(1, 'b')
print('a =', a)
a.insert(100, 'c')
print('a =', a)
a.insert(-1, 'd')
print('a =', a)
a.insert(-100, 'e')
print('a =', a)

a.remove('e')
print('a =', a)
# a.remove('!!!!')    # ValueError: list.remove(x): x not in list


# Sort
a = [2, 1, 3]
print('a =', a)
a.sort()
print('a =', a)
a.sort(reverse=True)
print('a =', a)

a = [2, 1, 'b', 'a']
# a.sort()        # TypeError: '<' not supported between instances of 'str' and 'int'

a = ['b', 'B', 'a', 'A']
a.sort()
print('a =', a)
a.sort(key=str.lower)
print('a =', a)


# Converting Tuple and List
a = [1, 2]
print('a =', a)
print('type of a =', type(a))
a = tuple(a)
print('a =', a)
print('type of a =', type(a))
a = list(a)
print('a =', a)
print('type of a =', type(a))
a = list('list')
print('a =', a)
print('type of a =', type(a))
a = tuple('tuple')
print('a =', a)
print('type of a =', type(a))


# Copy
a = [1, 2]
b = a
print('a =', a)
print('b =', b)
a.append(3)
print('a =', a)
print('b =', b)

a = [1, 2]
b = copy.copy(a)
print('a =', a)
print('b =', b)
a.append(3)
print('a =', a)
print('b =', b)

a = [1, 2, [3, 4]]
b = copy.copy(a)
print('a =', a)
print('b =', b)
a[2].append(5)
print('a =', a)
print('b =', b)

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
print('a =', a)
print('b =', b)
a[2].append(5)
print('a =', a)
print('b =', b)


# Index
l = ['a', 'b', 'c']
print(l.index('b'))
# print(l.index('d'))     # ValueError: 'd' is not in list
