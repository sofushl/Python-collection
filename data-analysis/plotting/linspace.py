import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2- 4*x + 3

x_verdi = np.linspace(-5+(4/2), 5+(4/2), 11)
y_verdi = f(x_verdi)

print ("x   :", x_verdi)
print ("f(x):", y_verdi)

plt.scatter(x_verdi, y_verdi, label = 'punkter')
plt.plot(x_verdi, y_verdi, '--', c = 'red', label = 'f(x)')

plt.legend()
plt.grid()
plt.xlabel('x-akse')
plt.axhline(y=0, color = 'black')
plt.axvline(x=0, color = 'black')
plt.ylabel('y-akse')
plt.show()
