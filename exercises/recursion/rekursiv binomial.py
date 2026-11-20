n = int(input())
k = int(input())

def fun(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return fun(n - 1, k - 1) + fun(n-1, k)

print(fun(n,k))