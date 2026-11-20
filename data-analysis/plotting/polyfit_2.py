import numpy as np

def f(x):
    return a*x**2+b*x+c

x = [1,2,3]
y = [7,20,39]

a,b,c = np.polyfit(x,y,2).round(decimals=5)

print (a,b,c)
print("a) " + str(f(4)))
print("b) " + str(f(20)))

counter = 0

for i in range(1,21):
    counter += f(i)

print("c) " + str(counter))
counter = 0
i = 0

while counter < 10000:
    i += 1
    counter += f(i)

print ("d) " + str(i))
