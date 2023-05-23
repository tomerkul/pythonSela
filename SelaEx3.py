def duplicates_Check(a=[]):
    newList = []
    num = input("Enter a number:")
    for i in range(len(a)):
        x = a.pop()
        if x in a:
            pass
        elif (int(x) <int(num)):
            newList.append(x)
    return newList

w = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(duplicates_Check(w))