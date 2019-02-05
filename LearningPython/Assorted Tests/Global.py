a = 'global'


def makeLocal():
    global a
    a = 'local'


print(a)
makeLocal()
print(a)
