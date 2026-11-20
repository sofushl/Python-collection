import numpy as np
import matplotlib.pyplot as plt

measurement = "Sound level oscillation"
interval = 0.1
filename = "mufile.txt"

def readdata(filename):
    data = []
    with open(filename,"r") as f:
        for element in f:
            data.append(float(element))
    data = np.array(data)
    return data

def plotdata(data, measurement, intervalmin):
    t = np.array(range(1, len(data)+1))/60*intervalmin
    plt.grid()
    plt.plot(t, data, c = "red", label = measurement)
    plt.xlabel("Time[min]", fontsize = 20)
    plt.ylabel(measurement, fontsize = 16)
    plt.legend()
    plt.tight_layout()
    plt.show()


def readplot(filename, measurement, intervalmin):
    data = readdata(filename)
    plotdata(data, measurement, interval)


readplot(filename, measurement, interval)
