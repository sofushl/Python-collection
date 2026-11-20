import matplotlib.pyplot as plt
import numpy as np

V = {
    1: [8, 25, 8], 2: [31, 10, 5], 3: [19, 23, 3], 4: [4, 20, 2], 5: [9, 24, 4], 6: [10, 20, 8], 7: [40, 22, 8], 
    8: [35, 22, 8], 9: [10, 15, 2], 10: [8, 16, 10], 11: [17, 25, 7], 12: [6, 14, 7], 13: [35, 25, 5], 
    14: [31, 24, 1], 15: [29, 16, 8], 16: [30, 21, 6], 17: [13, 20, 6], 18: [34, 25, 0], 19: [37, 11, 2], 
    20: [0, 22, 4], 21: [32, 22, 5], 22: [20, 13, 0], 23: [23, 17, 15], 24: [8, 12, 1], 25: [27, 20, 0],
    26: [34, 20, 4], 27: [4, 24, 3], 28: [22, 15, 1], 29: [38, 23, 8], 30: [29, 21, 3], 31: [26, 13, 10]}

nedbor = [] # Lister for grafering og variabler for sammenlikning
temp = []
vind = []
dag = []
maxV = [1]
minT = [1]
totT=0

for i in range(1,32): # Fyller ut listene med verdier løpende
    nedbor.append(V[i][0])
    temp.append(V[i][1])
    vind.append(V[i][2])
    dag.append(i)

    totT += V[i][1]

    if V[i][0] < V[minT[0]][0]: # Sammenlikner hver verdi med laveste/høyeste intil videre
        minT = [i]              # for å finne høyeste/laveste veri(er) av alle
    elif V[i][0] == V[minT[0]][0]:
        minT.append(i)

    if V[i][2] > V[maxV[0]][2]: #-----||-----
        maxV = [i]
    elif V[i][2] == V[maxV[0]][2]:
        maxV.append(i)

gjT = totT/31 # Regner gjennomsnittstemperatur ut i fra all temperatur iløpet av måneden

print("{:<20}{:<20}{:<20}{:<}".format("Dato", "Temperatur", "Nedbør", "Vindstyrke")) # printer ut etikketer øverst

for i in range(len(dag)): # printer all informasjonen på en organisert måte
    print("{:<20}{:<20}{:<20}{:<}".format(dag[i], str(temp[i]) + "\u00b0C", str(nedbor[i]) + "mm", str(vind[i]) + "m/s"))

print("{:<20}{:<20}{:<20}{:<}".format("Dato", "Temperatur", "Nedbør", "Vindstyrke")) # printer ut etikketer nederst

fig, (ax1, ax2, ax3) = plt.subplots(3) # lager et sett med plots, slik grafene ikke er i veien for hverandre
fig.suptitle('Værdata')

ax1.plot(dag, temp, c="red", label="Temperatur (\u00b0C)")  # Graferer alle dataene for en fin og oversiktlig måte
ax1.grid()                                                  # slik man tydelig kan se utviklingen.
ax1.legend(loc='upper left', frameon = False) 

ax2.plot(dag, nedbor, c="blue", label="Nedbør (mm)")
ax2.grid()
ax2.legend(loc='upper left', frameon = False)

ax3.plot(dag, vind, c="lightblue", label="Vindstyrke (m/s)")
ax3.grid()
ax3.legend(loc='upper left', frameon = False)

print("\n", end="")

print("Lukk grafen for å gå videre.")

plt.show()

print("\n", end="")

print(f"Gjennomsnittstemperaturen var: {gjT:.0f}\u00b0C")

print("\n", end="")

print(f"Lavest temperaturmåling var {V[minT[0]][0]}\u00b0C, det ble målt på dateoen(e):")
for i in minT:
    print(i, end="  ")

print("\n")

print(f"Høyest vindstyrke målt var {V[maxV[0]][2]}m/s, det ble målt på datoen(e):")
for i in maxV:
    print(i, end="  ")