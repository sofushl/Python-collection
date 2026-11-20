def f(x):
    return ((x**3-3)/3) # definerer utrykket som f(x) slik det ser finere ut i kode

for i in range(0, 21): # en løkke som repiteres 21 ganger hvor variabel i starter som 0 og slutter som 20
        if i % 2 == 0: # sjekker at vi har et partall ved å bruke modulo som regner ut rest fra divisjon. Hvis et tall delt på 2 har rest er det et oddetall, vi ønsker bare partall her
            print ("f(", i, ")=", round(f(i),2)) # printer it f( (tallet "i" er nå) )= verdien som kommer ut om vi setter in tallet i for x i funksjonen og avrunder den til nærmeste tall med 2 desimaler
            
