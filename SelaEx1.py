num = input("Enter a number:")
b = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < int(num):
        b.append(i)
print(b)
