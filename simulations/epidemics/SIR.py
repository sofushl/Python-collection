import numpy as np
import matplotlib.pyplot as plt

N = 250
I = 3
R = 0
S = N - I - R

tid = 100
a = 0.003
b = 0.2

mottakelige = [S]
infiserte = [I]
blitt_friske = [R]

t = np.linspace(1, tid, tid)

for i in range(1, tid):
    I = I+a*I*S - b*I
    infiserte.append(I)
    S = S - a*I*S
    mottakelige.append(S)
    R =  R + b*I
    blitt_friske.append(R)

print("2.")
print("For å bli frisk må man ha vært syk.")
print("Så det totale antallet infiserte må være lik antallet blitt friske,")
print("når infiserte er lik 0")
print(round(I,2)==0)
print("I = ",round(I,2),"R = ",round(R,2))
print("3.")
print("S+I+R = ", S + I + R, "N = 250")

plt.plot(t, infiserte, label = "Infiserte")
plt.plot(t, mottakelige, label = "Mottakelige")
plt.plot(t, blitt_friske, label = "blitt_friske")
plt.xlabel("Antall uker")
plt.ylabel("Antall smittede")
plt.legend()
plt.grid()
plt.show()
