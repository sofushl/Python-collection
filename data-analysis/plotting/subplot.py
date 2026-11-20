from pylab import *

# a), laster opp data i to liser og printer dem ut
# data = loadtxt("C:\Users\sofus\OneDrive - Trøndelag fylkeskommune\Documents\Code\ProgModX\matplotlib\kloss_data.txt", float,skiprows=1,delimiter=";")
# t = data[:, 0]
# s = data[:, 1]

t = [0.501, 0.551, 0.601, 0.651, 0.702, 0.752, 0.802, 0.852]
s = [0.218, 0.339, 0.444, 0.530, 0.598, 0.649, 0.684, 0.701]

print ("a)")
print ("t / s: ", t)
print ("s / m: ", s)

# b), bruker løkke + definisjonen av den deriverte "metoden"
#     til å fylle verdiene inn i lister
n = len(t)
v = zeros(n)
a = zeros(n-2)

for i in range(n-1):
    v[i] = (s[i+1] - s[i]) / (t[i+1] - t[i])

for i in range(n-2):
    a[i] = (v[i+1] - v[i]) / (t[i+1] - t[i])

print ("b)")
print ("v / m/s: ", v)
print ("s / m/s^2: ", a)

# c), Deler summen av alle aksellerasjonsverdiene på mengden punkter
#     for å finne gjennomsnittet
avga = mean(a)

print ("c)")
print ("Gjennomsnittsaksellerasjonen er: ", round(avga, 3))

#definerer en andregradsfunksjon og bruker polyfit til å finne abc verdiene
def f(x):
    return anum*x**2+bnum*x+cnum

anum,bnum,cnum = np.polyfit(t,s,2).round(decimals=5)

print("d) ")
print("s(t) = "+ str(round(anum,3))+ "x^2 + "+ str(round(bnum,3))+"x + "+ str(round(cnum,3)))

#definerer de deriverte v og a
def df(x):
    return anum*2*x+bnum

def ddf(x):
    return anum*2

#putter funksjonene inn i "detaljerte" lister
tlist = np.linspace(t[0], t[-1], len(t)*10)
slist = f(tlist)
vlist = df(tlist)

#setter opp subplots og fyller dem med relevante punkter og grafer
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('e) Plot data')

ax1.set_title("Distance")
ax1.scatter(t, s, label= "logged positions")
ax1.plot(tlist,slist, label = "s / m")
ax1.legend()
ax1.grid()

ax2.set_title("Velocity")
ax2.scatter(t, v, label= "logged positions",c="g")
ax2.plot(tlist,vlist,label = "v / m/s", c="g")
ax2.legend()
ax2.grid()

alist = zeros(n-2)
j = 0
for i in (t[0:n-2]):
    alist[j] = ddf(tlist)
    j += 1


ax3.set_title("Acceleration")
ax3.scatter(t[0:n-2],a,label = "logged positions",c ="r")
ax3.plot(t[0:n-2], alist, label= "f'' / a / m/s^2",c="r")
ax3.plot(t[0:n-2],a,"--",c ="r")
ax3.legend()
ax3.grid()

fig.tight_layout()
show()
