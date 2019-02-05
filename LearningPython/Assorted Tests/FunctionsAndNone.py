# Returns int
def func1(num):
    return num + 1


# Has a return statement but returns nothing
def func2():
    return


# No return statement
def func3():
    print('')


a = func1(1)
b = func2()
c = func3()

print('a: ', a)
print('b: ', b)
print('c: ', c)



# Call function before definition

# do()                # NameError: name 'do' is not defined

def do():
    print('doing')

do()



