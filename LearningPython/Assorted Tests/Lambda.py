sqr = lambda x: x**2
print(sqr(10))              # 100

print((lambda x: x**2)(4))  # 16

sum = lambda x, y: x+y
print(sum(1, 2))            # 3


def multi(n):
    return lambda x : x * n


fPointer = multi(10)        # <function multi.<locals>.<lambda> at 0x1086e6620>
print(fPointer)
print(fPointer(2))          # 20
print(fPointer(5))          # 50

