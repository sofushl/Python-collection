#Bruker numpy sin absoluttverdi utregner:
from numpy import abs

ke = 8.99e9
Q = 7.0e-9
q = -5.0e-9
d = 4.0e-2
R = 2.0e-2
m = 1.0e-3
v = 0
t = 0
dt = 0.01
p = R # starter med p = R, der p er y posisjon


while True: # løkke der akselerasjonen blir funnet og lagt til eller trukket fra farten
    a = (2*ke*R*Q*abs(q))/(m*(d**2+R**2)**(3/2))
    if p > 0: # Dersom posisjonen er over x aksen skal den nedover og a trekkes fra v
        v-=a*dt
    elif p < 0: # Ellers skal den opp og a legges til v
        v+=a*dt
    p+=v*dt
    t+=dt

    if round(p,15) >= R: # siden utregnignen ikke er helt nøyaktig runner jeg litt av
        print(p) # printer til slutt for å sikre at det er riktig
        break
    else:
        print(p) # printer underveis for å sikre at det kjører

print(t)