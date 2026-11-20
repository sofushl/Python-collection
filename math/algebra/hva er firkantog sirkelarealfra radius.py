from math import pi

r = float(input('Hva er radiusen: '))

s = round(pi*r**2, 3)
f = round(r+r*r+r, 3)

print ('Areal av sirkel er: ' +  str(s) + " og areal av firkant er: " + str(f))
