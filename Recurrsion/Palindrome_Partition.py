s = "aabb"

def isPalindrome(stri):
    if stri == stri[::-1]:
          return True
    else:
         return False

res = []
def fun(i, haf=[]):
    if i==len(s):
        res.append(haf[:])
        return
    for j in range(i,len(s)):
        if isPalindrome(s[:j+1]):
            haf.append(s[:j+1])
            fun(j+1)
            haf.pop()

fun(0)
return res
