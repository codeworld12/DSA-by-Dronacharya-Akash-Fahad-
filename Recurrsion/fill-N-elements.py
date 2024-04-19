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





