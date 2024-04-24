arr = [3, 34, 4, 12, 5, 2]
target = 30
n = len(arr)
has=[]
ans = []
def fun(i):
    if sum(has) > target:
        return
    if sum(has) == target:
        ans.append(has.copy())
        return 
    if n == i:
        return False
    has.append(arr[i])
    fun(i+1)
    has.pop()
    fun(i+1)
    return ans 
    

res = fun(0)
if len(res) > 0:
    print(True)
else:
    print(False)