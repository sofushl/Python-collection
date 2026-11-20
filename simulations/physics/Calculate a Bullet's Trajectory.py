import random
import math

Velocity = 400 #standard hastighet målt i meter per sekund
Gravity = 9.8 #tyngdekraften på jorda
Coefficiency_of_bullet = 0.295 #generelt skudd
Air_density = 1.2 #kg/kubikkmeter ved normal temperatur og trykk
Skudd_areal = 4.8*10**-5 #regnes ut ved Pi*r^2, areal for sirkel. 4.8*10**-5 er .308 kaliber
Masse_av_skudd = 0.016 #generelt skudd

print ("Du har en .308 Winchester og skal se hvor langt du kan skyte!")

while True:
    Planet = str(input("Hvilken planet er du på? "))
    if Planet == "jorda":
        g = 9.81
        p = 1.3
    elif Planet == "mars":
        g = 3.7
        p = 0.02
    elif Planet == "venus":
        g = 8.9
        p = 65
    elif Planet == "merkur":
        g = 3.7
        p = 0
    elif Planet == "pluto":
        if random.randint(1, 10) == 1:
            print("PLUTO ER IKKE EN PLANET PLUTO ER IKKE EN PLANET PLUTO ER IKKE EN PLANET PLUTO ER IKKE EN PLANET")
        g = 0.6
        p = 0
    elif Planet == "sola":
        g = 274
        p = 0.1
    elif Planet == "saturn":
        g = 10.4
        p = 0
    elif Planet == "jupiter":
        g = 24.8
        p = 0.5
    elif Planet == "uranus":
        g = 8.9
        p = 0.4
    elif Planet == "neptun":
        g = 11.2
        p = 0.5
    elif Planet == "månen":
        g = 1.6
        p = 0
    else:
        print ("invalid planet, vi bruker jorda")
        g = 9.8
        p = 1.3
        
    v = Velocity
    c = Coefficiency_of_bullet
    a = Skudd_areal
    m = Masse_av_skudd

    def f(h):
        return v*math.sqrt(2*h/g) - (c*p*a*v**2*(math.sqrt(2*h/g))**2)/(2*m)

    h = float(input("Hvor høyt holder du hånden din i meter? "))

    print("Hvis du holder hånda di ", round(h, 1), " meter over bakken")
    print ("Er skuddistansen ", round(f(h)), "meter")

    r = str(input("Vil du skyte igjen? y/n: "))
    if r == "n":
        break
        
        
