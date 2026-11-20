#definerer funskjonen
def f(x):
    return -x**2 + 3*x +4

#bestemmer verdiene som utregningen skal bruke
n = 100
a = 0
b = 6
dx = (b-a)/n

#setter "tellerene" til 0
arealo = 0
arealu = 0
arealm = 0
arealt = 0

#legger til arealet for hver n rektangel
for i in range(n):
    arealo += dx*f(a+(i+1)*dx)
    arealu += dx*f(a+i*dx)
    arealm += dx*f(a+(i+0.5)*dx)
    arealt += (f(a+i*dx)+f(a+(i+1)*dx))*dx/2

#printer ut resultatet
print(arealo)
print(arealu)
print(arealm)
print(arealt)
