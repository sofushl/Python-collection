q=1.602e-19
m=9.109e-31
v=8e6
t=0
B=3.20e-3
dB=0.3e-3

for n in range(15):
    B += dB
    r = (m*v)/(q*B)
    t += (2*3.14*r)/v

print(t)