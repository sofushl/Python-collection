n = int(input())

def Tri(x):
    if x == 0 or x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return Tri(x-1) + Tri(x-2) + Tri(x-3)

print(Tri(n))