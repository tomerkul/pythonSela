def fibonaccilist():
    fibo = [0]
    a , b = 1,1
    numberof = int(input("how many fibonacci numbers? "))
    for i in range(numberof):
        fibo.append(a)
        a,b = b,a+b
    return fibo
print(fibonaccilist())