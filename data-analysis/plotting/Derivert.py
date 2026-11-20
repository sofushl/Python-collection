import matplotlib.pyplot as plt
import numpy as np
e = 2.71828

def f(x):
    return -3*x**3+4*x**2-5*x+10

def derivert(a):
    return (f(a+dx)-f(a))/dx

def dersym(a):
    return (f(a+dx)-f(a-dx))/2*dx

dx = 1E-8
print ("b) ", "-9*x**2+8*x-5")


x = np.linspace(-5,5,100)
y = f(x)
dfy = derivert(x)
plt.plot(x, y, label = "f(x)", c = "red",)
plt.plot(x, dfy, label = "f'(x)",c = "blue")
plt.grid()
plt.legend()
plt.title("Funkjsoner")
plt.xlabel('x-akse')
plt.axhline(y=0, color = 'black')
plt.axvline(x=0, color = 'black')
plt.ylabel('y-akse')
plt.show()
