# 1) Appproach

# coun = 0
# def fun(n,a):
#     global coun
#     if a == 1 and coun <1:
#         return True
#     if coun > 0:
#         return False
#     if n % a == 0:
#         coun += 1
#     return fun(n, a-1)
# n  = int(input("enter : "))
# ans = fun(n, n-1)

# if ans:
#     print("It is prime number")
# else:
#     print("It is not prime number")

# 2) Approach

# Prime Number
def fun(n,a):
    if a == 1:
        return True
    if n % a == 0:
        return False
    return fun(n, a-1)
n  = int(input("enter : "))
ans = fun(n, n-1)

if ans:
    print("It is prime number")
else:
    print("It is not prime number")