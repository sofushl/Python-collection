list =  [1,2,3,4,5,6,7,8,9]            #list(map(int, input().split()))

def fun(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[-1] + fun(l[:-1])

print(fun(list))