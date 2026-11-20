list = [3,7,2,4]  #list(map(int, input().split()))

def fun(l):
    if len(l) == 1:
        return 0
    else:
        return l[-1]*l[-2] + fun(l[:-1]) 


print(fun(list))