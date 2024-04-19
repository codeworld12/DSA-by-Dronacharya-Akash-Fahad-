# fill array of n elements

li = []
def fun(n):
    if n == 0:
        li.append(n)
        return li
    else:
        li.append(n)
    return fun(n-1)
n = int(input())
ans = fun(n)
print(sorted(ans))

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











