import shelve

sFile = shelve.open('shelve_obj')

names = ['alice', 'bob', 'catie', 'Donuld']
sFile['names'] = names

sFile.close()


sFile = shelve.open('shelve_obj')
print(type(sFile))
print(sFile.keys())
print(list(sFile.keys()))
print(sFile.values())
print(list(sFile.values()))
print(sFile['names'])
sFile.close()

l = []
for i in range(1000):
    l = l + [i]
print(l)
sFile = shelve.open('shelve_obj')
sFile['lists'] = l
sFile.close()


sFile = shelve.open('shelve_obj')
print(type(sFile))
print(sFile.keys())
print(list(sFile.keys()))
print(sFile.values())
print(list(sFile.values()))
print(sFile['lists'])
sFile.close()


sFile = shelve.open('shelve_obj')
del sFile['names']
print(type(sFile))
print(sFile.keys())
print(list(sFile.keys()))
print(sFile.values())
print(list(sFile.values()))
print(sFile['lists'])
sFile.close()
