def sqr_func(x):
    return x**2


a = [1, 2, 3]

b = [x**2 for x in a]
print(b)                            # [1, 4, 9]

c = [sqr_func(x) for x in a]
print(c)                            # [1, 4, 9]

c = map(sqr_func, a)
print(c)                            # <map object at 0x10e944550>
print(list(c))                      # [1, 4, 9]

d = map(lambda x: x**2, a)
print(list(d))                      # [1, 4, 9]


a = ['a', ' b ', '  c']

b = [s.strip() for s in a]
print(b)                            # ['a', 'b', 'c']

c = map(str.strip, a)
print(list(c))                      # ['a', 'b', 'c']

d = map(lambda s: s.strip(), a)
print(list(d))                      # ['a', 'b', 'c']


a = [['a', ' b '], ['  c', 'd ', 'e']]   # [['a', ' b '], ['  c', 'd ']]
b = [len(row) for row in a]
print(b)                            # [2, 3]

b = [[s.strip() for s in row] for row in a]
print(b)                            # [['a', 'b'], ['c', 'd', 'e']]

c = [list(map(lambda s: s.strip(), row)) for row in a]
print(c)                            # [['a', 'b'], ['c', 'd', 'e']]


