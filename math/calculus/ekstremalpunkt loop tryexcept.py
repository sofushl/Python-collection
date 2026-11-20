import matplotlib.pyplot as plt
import numpy as np

while True:

    #spør brukeren om verdier for f(x) igjen og igjen fram til det er heltall som returneres
    while True:
        try:
            a = float(input("Choose a: "))
            b = float(input("Choose b: "))
            c = float(input("Choose c: "))
            d = float(input("Choose d: "))
            break
        except Exception:
            print("Du må skrive et heltall")

    #definerer f(x)
    def f(x):
        return a*x**3+b*x**2+c*x+d

    #definerer den deriverte
    def derivert(a):
        return (f(a+dx)-f(a))/dx

    dx = 1E-8


    #setter opp x og y verdier for f(x)
    funx = np.linspace(-5,5,100)
    funy = f(funx)
    dery = derivert(funx)

    #setter opp plotet og viser det
    plt.plot(funx, funy, label = "f(x)", c = "red",)
    plt.plot(funx, dery, label = "f'(x)", c = "blue",)

    plt.grid()
    plt.legend()
    plt.xlabel('x-akse')
    plt.ylabel('y-akse')

    plt.axvline(x=0, color = 'black')
    plt.show()

    #spør brukeren hvilke punkter som skal brukes som utgangspunkt igjen og igjen fram til det er heltall som returneres
    while True:
        try:
            x_vinput = int(input("Choose left starting point: "))
            x_hinput = int(input("Choose right starting point: "))
            break
        except Exception:
            print("Du må skrive et heltall")

    x_v = x_vinput
    x_h = x_hinput
    x = (x_h+x_v)/2

    #bruker halveringsmetoden til å finne nullpunktet med 10 desimals nøyaktighet
    while round(f(x),10) != 0:
        print (round(x, 10))
        if f(x_v)*f(x)>0:
            x_v = x
        else:
            x_h = x
        x = (x_h+x_v)/2

    Nullpunkt = (round(x, 2))

    #nullstiller utgangspunktene til brukerens input
    x_v = x_vinput
    x_h = x_hinput
    x = (x_h+x_v)/2

    #finner nullpunkt i den deriverte / ekstremalpunkt i f(x)
    while round(derivert(x),10) != 0:
        print (round(x, 10))
        if derivert(x_v)*derivert(x)>0:
            x_v = x
        else:
            x_h = x
        x = (x_h+x_v)/2

    Ekstremalpunkt = (round(x, 2))

    #bruker den dobbeltderiverte til å finne ut hva slags ekstremalpunkt vi har
    def dobbeltderivert(a):
        return (derivert(a+dx)-derivert(a))/dx

    if dobbeltderivert(x) < 0:
        Ekstremalpunkttype = "Toppunkt"
    elif dobbeltderivert(x) > 0:
        Ekstremalpunkttype = "Bunpunkt"
    else:
        Ekstremalpunkttype = "Terrassepunkt"

    #printer ut resultatet
    print (f"Du fant nullpunkt i {Nullpunkt} og et {Ekstremalpunkttype} i {Ekstremalpunkt}")

    #spør brukeren om de vil la programmet fortsette og sette inn nye utgangspunkt uavhengig kapitalisering av svaret
    if input("Do you wish to start over? y/n ").lower() == "n":
        break
