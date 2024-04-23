print("Not able to get exact output")

n = 4
k = 2
num = [i for i in range(1, n+1)]
print(num)
res = []
def fun(i, haf):
    print(i)
    if i == len(num):
        return
    if len(haf) == k:
        res.append(haf.copy())
        return
    haf.append(num[i])
    fun(i+1, haf)
    # print("haf", haf)
    haf.pop()
    fun(i+1,haf)
    return res

print(fun(0, []))

# O/P
# [[1, 2], [1, 3], [2, 3]]
