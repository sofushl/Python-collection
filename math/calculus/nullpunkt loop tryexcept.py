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

    #setter opp x og y verdier for f(x)
    funx = np.linspace(-5,5,100)
    funy = f(funx)

    #setter opp plotet og viser det
    plt.plot(funx, funy, label = "f(x)", c = "red",)
    plt.grid()
    plt.legend()
    plt.xlabel('x-akse')
    plt.ylabel('y-akse')
    plt.axhline(y=0, color = 'black')
    plt.axvline(x=0, color = 'black')
    plt.show()

    #spør brukeren hvilke punkter som skal brukes som utgangspunkt igjen og igjen fram til det er heltall som returneres
    while True:
        try:
            x_v = int(input("Choose left starting point: "))
            x_h = int(input("Choose right starting point: "))
            break
        except Exception:
            print("Du må skrive et heltall")
    x = (x_h+x_v)/2

    #bruker halveringsmetoden til å finne nullpunktet med 10 desimals nøyaktighet
    while round(f(x),10) != 0:
        print (round(x, 10))
        if f(x_v)*f(x)>0:
            x_v = x
        else:
            x_h = x
        x = (x_h+x_v)/2


    print (round(x, 2))

    #spør brukeren om de vil la programmet fortsette og sette inn nye utgangspunkt uavhengig kapitalisering av svaret
    if input("Do you wish to start over? y/n ").lower() == "n":
        break
