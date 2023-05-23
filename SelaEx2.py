a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
if len(a) <= len(b):
    length = len(a)
    big = b
    small = a
else:
    length = len(b)
    big = a
    small = b
for i in range(length):
    z = small.pop()
    if z in small:
        pass
    else:
        if z in big:
            c.append(z)
print(c)
