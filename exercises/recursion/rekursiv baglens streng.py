letters = list([*str(input())])

def fun(l):
    if len(l) == 1:
        return l[0]
    else:
        return [l[-1], ''.join(list(fun(l[:-1])))]


print(''.join(list(fun(letters))))

