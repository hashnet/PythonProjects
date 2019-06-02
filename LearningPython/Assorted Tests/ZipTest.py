x = [1, 2, 3]
y = ["a", "b", "c"]
zipped = zip(x, y)

print(type(zipped))     # <class 'zip'>

for item in zipped:
    print(item)
# (1, 'a')
# (2, 'b')
# (3, 'c')

print(list(zipped))     # []    # zipped is exhausted while iterated

zipped = zip(x, y)
print(list(zipped))     # [(1, 'a'), (2, 'b'), (3, 'c')]

zipped = zip(x, y)      # zipped is again exhausted
print(tuple(zipped))    # ((1, 'a'), (2, 'b'), (3, 'c'))


# List of Tuples
print(list(zip(x, y)))                          # [(1, 'a'), (2, 'b'), (3, 'c')]

# List of Lists
print([list(a) for a in zip(x, y)])             # [[1, 'a'], [2, 'b'], [3, 'c']]
print(list(map(lambda a: list(a), zip(x, y))))  # [[1, 'a'], [2, 'b'], [3, 'c']]
print(list(map(list, zip(x, y))))               # [[1, 'a'], [2, 'b'], [3, 'c']]

# tuple of Lists
print(tuple([list(a) for a in zip(x, y)]))      # ([1, 'a'], [2, 'b'], [3, 'c'])
print(tuple(list(a) for a in zip(x, y)))        # ([1, 'a'], [2, 'b'], [3, 'c'])
print(tuple(map(lambda a: list(a), zip(x, y)))) # ([1, 'a'], [2, 'b'], [3, 'c'])
print(tuple(map(list, zip(x, y))))              # ([1, 'a'], [2, 'b'], [3, 'c'])

# Tuple of Tuples
print(tuple(zip(x, y)))                         # print(tuple(zip(x, y)))


