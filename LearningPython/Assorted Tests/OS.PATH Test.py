import os

p = os.getcwd()
print(p)


# Absolute Path
p = os.path.abspath('.')
print(p)

p = os.path.abspath('..')
print(p)

p = os.path.abspath('../diffFolder')    # Doesn't matter if the folder exists
print(p)

print(os.path.isabs('/'))
print(os.path.isabs('.'))
print(os.path.isabs('c:\\'))


# Relative Path
p = os.path.relpath('/a/b/d', '/a/c/e')
print(p)
p = os.path.abspath(p)
print(p)

p = os.path.relpath('/a/b', '/a')
print(p)

p = os.path.relpath('/a/b', 'c')
print(p)

p = os.path.relpath('/a/b', '.')
print(p)
p = os.path.relpath('/a/b', os.getcwd())
print(p)

p = os.path.relpath('c', '/a/b')
print(p)

p = '/a/b/c/d.dmz'
print(os.path.dirname(p))
print(os.path.basename(p))
p = '/a/b/c'
print(os.path.dirname(p))
print(os.path.basename(p))
p = '/a/b/c/d.dmz'
t = os.path.split(p)
print(t)
t = (os.path.dirname(p), os.path.basename(p))
print(t)

p = '/a/b/c/d.dmz'
s = p.split(os.path.sep)
print(s)


# Size
l = os.path.getsize('/Users/maidul/PythonProjects/Test Modules/OS.PATH Test.py')
print(l)
l = os.path.getsize('OS.PATH Test.py')
print(l)
# l = os.path.getsize('/anyfile') # FileNotFoundError: [Errno 2] No such file or directory: '/anyfile'
l = os.path.getsize('/Users/maidul/PythonProjects/Test Modules')
print(l)


# Folder Contents
d = os.listdir('/Users/maidul/PythonProjects/Test Modules')
print(d)
# d = os.listdir('/anydir')       # FileNotFoundError: [Errno 2] No such file or directory: '/anydir'
myDir = '/Users/maidul/PythonProjects/Test Modules'
tot = 0
for file in os.listdir(myDir):
    tot += os.path.getsize(os.path.join(myDir, file))
print(tot)


# Path Validity
print(os.path.exists('/a/b'))                                                       # False
print(os.path.exists('/Users/maidul/PythonProjects/Test Modules/'))                 # True
print(os.path.exists('/Users/maidul/PythonProjects/Test Modules/OS.PATH Test.py'))  # True
print(os.path.isdir('/Users/maidul/PythonProjects/Test Modules/'))                  # True
print(os.path.isdir('/Users/maidul/PythonProjects/Test Modules/OS.PATH Test.py'))   # False
print(os.path.isfile('/Users/maidul/PythonProjects/Test Modules/'))                 # False
print(os.path.isfile('/Users/maidul/PythonProjects/Test Modules/OS.PATH Test.py'))  # True


