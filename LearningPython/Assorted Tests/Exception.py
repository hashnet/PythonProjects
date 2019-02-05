import sys


def onebynum(num):
    return 1 / num


a = onebynum(2)
# b = onebynum(0) #ZeroDivisionError: division by zero
print('a =', a)


def onebynumtry(num):
    try:
        return 1 / num
    except ZeroDivisionError:
        print('Invalid arguments.')


b = onebynumtry(2)
print('b =', b)
b = onebynumtry(0)
print('b =', b)


# Sys.exc_info()
try:
    a = 1/0
except:
    print(sys.exc_info())
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])



# sys.exit()
try:
    a = 1/1
except ZeroDivisionError:
    print('infinity')
    sys.exit()

