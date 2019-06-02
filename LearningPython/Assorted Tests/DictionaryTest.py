import pprint

a = {'name': 'alice', 'age': 30}
print(a['name'])
# print(a[name])      # NameError: name 'name' is not defined

a = {0: 'index 0',
     'one': 'index 1',
     2: 2
     }
print(a[0])
print(a['one'])
print(a[2])
# print(a[3])        # KeyError: 3


# The keys(), values(), and items() Methods
a = {'name': 'alice', 'age': 30, 2: None}
print(a.keys())
print(a.values())
print(a.items())

for i in a.keys():
    print('{} = {}'.format(i, a[i]))

for i in a.values():
    print(i)

for i in a.items():
    print(i)

for i in a.items():
    print('{} = {}'.format(i[0], i[1]))

print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))

for k, v in a.items():
    print('{} = {}'.format(k, v))


# In or Not In
a = {'name': 'alice', 'age': 30, 2: None}
print('name' in a.keys())
print(None in a.values())
print(('age', 30) in a.items())
print(['age', 30] in [list(i) for i in a.items()])      # using list comprehension


# Get
a = {'name': 'alice', 'age': 30, 2: None}
if 'name' in a.keys():
    b = a['age']
else:
    b = 0
print('b =', b)

print(a.get('age', 0))
print(a.get('ages', 0))


# SetDefault
a = {'name': 'alice', 'age': 30, 2: None}
if 'sex' not in a.keys():
    a['sex'] = 'male'
print('a =', a)

a = {'name': 'alice', 'age': 30, 2: None}
a.setdefault('sex', 'male')
print('a =', a)

a = {'name': 'alice', 'age': 30, 2: None}
a.setdefault('age', 10)
print('a =', a)


# Pretty Print
str = 'Today is a very good day'
count = {}
for c in str.lower():
    count.setdefault(c, 0)
    count[c] += 1
pprint.pprint(count)

# Iterators
a = {1: 'alice', 2: 'bob', 3: 'charlie'}
it = iter(a)
print(type(it))
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
print()
it = iter(a)
for x in it:
    print(x, end=' ')       #does the same as above
print()
it = a.items()
print(type(it))
print(it)


