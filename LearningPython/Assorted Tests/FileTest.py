import os

# Join Path
myPath = os.path.join('/', 'Users', 'maidul', 'PythonProjects', 'Test Modules', 'FileTest.py')
print(myPath)

# GETCWD and CHDIR
print(os.getcwd())

os.chdir('/Users/maidul/Test')
print(os.getcwd())

# os.chdir('/Users/unknownUser')      # FileNotFoundError: [Errno 2] No such file or directory: '/Users/unknownUser'


# MAKEDIRS and MKDIR
d = os.path.join(os.getcwd(), "Dir level 1", "Dir level 2", "Dir level 2")
print(d)
# os.mkdir(d)   # FileNotFoundError: [Errno 2] No such file or directory:
# '/Users/maidul/Test/Dir level 1/Dir level 2/Dir level 2'
d = os.path.join(os.getcwd(), "Dir level 1")
os.mkdir(d)

d = os.path.join(d, "Dir level 2", "Dir level 3")
# os.makedirs(dir)  # FileExistsError: [Errno 17] File exists: '/Users/maidul/Test/Dir level 1/Dir level 2/Dir level 2'
try:
    os.makedirs(d)
except FileExistsError:
    print('The folder already exists.')


