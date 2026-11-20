import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return a*x**3+b*x**2+c*x+d

x = [0,1,4,7,9,10,12,13,15,17,20,22]
y = [19,17,15,17,19,21,25,26,27,26,24,22]

a,b,c,d = np.polyfit(x,y,3).round(decimals=5)
print (a,b,c,d)


x_list = np.linspace(0, x[-1], 50)
y_list = f(x_list)

plt.scatter(x, y, label= "Temperaturmålinger")
plt.plot(x_list,y_list)
plt.legend()
plt.grid()
plt.show()
