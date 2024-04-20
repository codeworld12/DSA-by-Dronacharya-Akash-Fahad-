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





