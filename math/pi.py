from numba import njit

pi = 0
i = 1

@njit()
def findpi(pi,i):
    for j in range(10000000000):
        pi += 1/i
        i += 2
        overpi = pi*4
        pi -= 1/i
        i+=2
        underpi = pi*4
    return pi, i, underpi, overpi


while True:
    pi, i, underpi, overpi = findpi(pi,i)

    realpi = []
    ref = list(str(underpi))
    for l in range(len(ref)):
        if ref[l] == list(str(overpi))[l]:
            realpi.append(ref[l])
        else:
            break
    
    print ('{:<30}{:<40}{:<40}{:40}{:<}'.format((str(int(i/4000000000)) + " Mrd"), underpi, overpi, "".join(realpi), len(realpi)))

