def fun(n):
    if n == 10:
        return n
    print(n, end=" ")
    return fun(n+1)
print(fun(1))