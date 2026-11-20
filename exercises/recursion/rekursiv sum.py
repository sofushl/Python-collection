n = int(input())


def fun(x):
    if x == 1:
        return 1
    else:
        return fun(x-1) + x


print(fun(n))