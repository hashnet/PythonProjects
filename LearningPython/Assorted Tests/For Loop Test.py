text = 'text'
for char in text:
    print(char, end=' ')    # t e x t
print()

lst = ['i', 'have', 2, ['book1', 'book2']]
for item in lst:
    print(item, end=' ')    # i have 2 ['book1', 'book2']
print()

print(range(10))            # range (0, 3)
print(range(2, 10))         # range (2, 10)
print(range(2, 10, 3))      # range(2, 10, 3)

for i in range(10):
    print(i, end=' ')       # 0 1 2 3 4 5 6 7 8 9
print()
for i in range(2, 10):
    print(i, end=' ')       # 2 3 4 5 6 7 8 9
print()
for i in range(2, 10, 3):
    print(i, end = ' ')     # 2 5 8
print()

# for/else
for n in range (2, 6):
    for x in range (2, n):
        if n%x == 0:
            print(n, '=', x, '*', int(n/x))
            break
    else:
        print(n, ' is prime')
# Output:
# 2  is prime
# 3  is prime
# 4 = 2 * 2
# 5  is prime