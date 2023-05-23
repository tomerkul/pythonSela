def myfunction(a=[]):
    sum = 0
    for i in a:
        if isinstance(i, int):
            sum = sum + int(i)
    return sum

a =[1,2,3,1,5]
print(sum(a))