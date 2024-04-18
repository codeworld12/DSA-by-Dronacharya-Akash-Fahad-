def fun(n):
    if n == 1:
        return n
    print(n, end=" ")
    return fun(n-1)
print(fun(10))