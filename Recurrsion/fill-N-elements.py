# fill array of n elements

n = int(input())
li = [0] * (n+1)        ## declaring array
def fun(n):
    if n == 0:
        li[n] = n
        return li
    li[n] = n
    return fun(n-1)

ans = fun(n)
print(ans)

# 2nd Approach

n = int(input())
li = [0] * (n+1)        ## declaring array
def fun(n):
    if n == 0:
        li[n] = n
        return li
    li[n] = n
    return fun(n-1)

ans = fun(n)
print(ans)

# 3rd Approach without zero
n = int(input())
li = [0] * n 
def fun(n):
    if n == 1:
        li[n-1] = n
        return li
    li[n-1] = n
    return fun(n-1)

print(fun(n))











