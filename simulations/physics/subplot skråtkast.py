from pylab import *

path = "Old\ProgModX\matplotlib\Data\skraattkast.txt"

data = loadtxt(path, float,skiprows=1,delimiter=";")
t = data[:, 0]
x = data[:, 1]
y = data[:, 2]
n = len(t)
fartx = zeros(n)
farty = zeros(n)
aks_y = zeros(n)



for i in range(n-1):
    fartx[i] = (x[i+1] - x[i]) / (t[i+1] - t[i])
    farty[i] = (y[i+1] - y[i]) / (t[i+1] - t[i])

for i in range(n-2):

    aks_y[i] = (farty[i+1] - farty[i]) / (t[i+1] - t[i])


fig, (ax1, ax2, ax3) = plt.subplots(3)

fig.suptitle('Vertically stacked subplots')

ax1.plot(t[0:n-2], fartx[0:n-2], label = "x")
ax1.grid()


ax2.plot(t[0:n-2], farty[0:n-2], label = "y")
xlabel("Tid (s)")
ylabel("Fart (m/s)")
ax2.grid()

ax3.plot(t[0:n-2], aks_y[0:n-2], label = "aks_y")
ax3.grid()
ax3.set_title("aksellerasjon y")

show()
