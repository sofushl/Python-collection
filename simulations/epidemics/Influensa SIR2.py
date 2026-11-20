import numpy as np
import matplotlib.pyplot as plt

path = "Old\ProgModX\matplotlib\Data\influensa.txt"

data = np.loadtxt(path,skiprows=2, delimiter=',')
x = data[:,0]
y = data[:,1]

tid = 48
N = 157759
a = 4.8/N #Spredningsraten
I = 3

S = N-I
mottakelige = [S]
infiserte = [I]
t = np.linspace(1,tid,tid)

for i in range(1,tid):
    I = I + a*I*S
    infiserte.append(I)
    S = S-a*I*S
    mottakelige.append(S)

plt.plot(t, infiserte, label = 'infiserte')
#plt.plot(t, mottakelige, label = 'Mottakelige')
plt.plot(x,y, label = 'ekte data')
plt.legend()
plt.show()
