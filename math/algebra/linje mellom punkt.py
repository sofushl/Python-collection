import numpy as np
import matplotlib.pyplot as plt

ay = int(input("ay="))
ax = int(input("ax="))
by = int(input("by="))
bx = int(input("bx="))

def fa(ax, ay, bx, by):
    if ax > bx:
        return (ax - bx)/(ay - by)
    elif ax < bx:
        return (bx - ax)/(by - ay)
    else:
        print ("user input syntax error")

def fb(a, ax, ay):
    return ay-a*ax


a = fa(ax, ay, bx, by)
b = fb(a, ax, ay)

if b > 0:
    f = (f"y = {a}x + {b}")
elif b < 0:
    f = (f"y = {a}x + {b}")
else:
    f = (f"y = {a}x")
def f(x):
    a*x+b
x_verdi = [ax, bx]
y_verdi = [ay, by]

plt.scatter(x_verdi, y_verdi, label = 'punkter')
plt.plot(x_verdi, y_verdi, '--', c = 'red', label = 'f(x)')

plt.legend()
plt.grid()
plt.xlabel('x-akse')
plt.axhline(y=0, color = 'black')
plt.axvline(x=0, color = 'black')
plt.ylabel('y-akse')
plt.show()
