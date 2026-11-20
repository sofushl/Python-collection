import numpy as np
import matplotlib.pyplot as plt

path = "Old\ProgModX\matplotlib\Data\influensa.txt"


data=np.loadtxt(path,skiprows=2,delimiter=",")
x = data[:,0]
y = data[:,1]

tid = 48
a = 0.000001
N = 157759
I = 3
R = 0
S = N - I - R

mottakelige = [S]
infiserte = [I]
blitt_friske = [R]
t = np.linspace(1, tid, tid)

for i in range(1, tid):
    I = I+a*I*S
    infiserte.append(I)
    S = S - a*I*S
    mottakelige.append(S)

plt.plot(t, infiserte, label = "Infiserte")
#plt.plot(t, mottakelige, label = "Mottakelige")
plt.plot(x,y)
plt.xlabel("Antall uker")
plt.ylabel("Antall smittede")
plt.legend()
plt.grid()
plt.show()
