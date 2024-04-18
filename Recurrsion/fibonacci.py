def fun(n):
    if n <= 1:
        return n
    a = fun(n-1)
    b = fun(n-2)
    c = a + b
    
    return c
print(fun(5))