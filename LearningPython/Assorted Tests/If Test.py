a = "alice"
n = 10

print(a == 10)
print(n == "alice")
# print(n > "alice")      # TypeError: '>' not supported between instances of 'int' and 'str'
# print(a > 10)           # TypeError: '>' not supported between instances of 'str' and 'int'
print(a < "bob")


a = 1
b = 2

if not a == 10:
    print(a)            # 1

if not b == 20:
    print(b)            # 2

if not a == 10 and not b == 20:
    print(a + b)        # 3

if not a == 10 and b == 20:
    print(a + b)        # nothing prints

if (not a == 10) and b == 20:
    print(a + b)        # nothing prints

if not (a == 10 and b == 20):
    print(a + b)        # 3

