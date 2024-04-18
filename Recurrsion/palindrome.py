s = "MALAYALAM"
i, j = 0, len(s)-1
def fun(s, i, j):
    # base case
    if i == j:
        return True
    if i >= j:
        return True
    
    if s[i].lower() == s[j].lower():
        return fun(s, i+1, j-1)
    else:
        return False

print(fun(s, i, j))