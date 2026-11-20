from math import sqrt
def f(x):
    return sqrt(x**2)

a = -2
b = 2
n = 4

delta_x = (b-a)/n
sum = 0

for i in range(1, n+1):
    sum += f(a+(i-1)*delta_x) * delta_x
    
print(f" {n} rektangler gir tilnærmingsverdien {sum:.1f}")