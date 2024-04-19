# Sum Of All Natural Numbers

# 1) With space
li = []
def fun(n):
    if n == 1:
        li.append(n)
        return li
    li.append(n)
    return fun(n-1)
fun(int(input()))
print(sum(li))

# 2) without using space
def fun(n):
    if n == 1:
        return n
    print(n)
    return n + fun(n-1)
    
print(fun(int(input())))




