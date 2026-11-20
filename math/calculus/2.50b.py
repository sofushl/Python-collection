def f(x):
    return x**2

a = 1
b = 5

n = 200
dx = (b-a)/n

s = 0

for i in range(1,n):
    a+=f(1 + (i-1)*dx)*dx

print (a)