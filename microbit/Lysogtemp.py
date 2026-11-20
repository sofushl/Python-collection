import numpy as np
import matplotlib.pyplot as plt

data1 = []
data2 = [] #Lager lister for de 2 dataene
flip = 0
with open("mufile.txt","r") as f:
    for element in f: #Løkke som seperer alle dataene på oddetalls linjer og partallslinjer inn i hver sin liste
        if flip == 0:
            data1.append(float(element))
            flip = 1
        else:
            data2.append(float(element))
            flip = 0
data1 = np.array(data1)
data2 = np.array(data2)

def graph(data, measurement):
    t = np.array(range(1, len(data)+1))*10 #Setter lengden (langs x aksen) på grafen basert på lendgen til dataene fra målingen
    plt.grid() #Setter visningsmodus
    plt.plot(t, data, c = "red", label = measurement) #Lager en graf
    plt.xlabel("Time[min]", fontsize = 20) #Navngit x aksen
    plt.ylabel(measurement, fontsize = 16) #Navngir y aksen
    plt.legend()
    plt.tight_layout() #Gjør grafen finere
    plt.savefig(measurement + "_graph.png", dpi = 300) #Lagrer grafen i .png fil med 300 PPI/DPI
    plt.show() #Viser grafen

graph(data1, "Temperature[\u00b0C]")
graph(data2, "Lightlevel[MonkMakes]")
