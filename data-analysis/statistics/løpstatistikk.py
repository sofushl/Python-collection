print("Velkommen til løperstatistikkprogrammet")

def sortnummer(nummer, tider): # Rekursiv funksjon som sorterer tidene
    minstnum = nummer[0]
    minst = tider[0]


    for i in range(len(nummer)):
        if tider[i] < minst:
            minst = tider[i]
            minstnum = nummer[i]

    tider.remove(minst)
    nummer.remove(minstnum)
    
    if len(nummer) > 0:
        liste = sortnummer(nummer, tider)
        liste.insert(0, minstnum)

    else:
        liste = [minstnum]
    return liste

ant = int(input("Hvor mange løpere: "))

nummer = []
navn = []

for i in range(ant): # Spør etter løpernavn
    print("")
    while True:
        try:
            nummer.append(int(input("Løpernummer: ")))
            if nummer[i] not in nummer[:i]:
                navn.append(str(input("Løpernavn: ")))  
                break
            else:
                nummer.pop()
                print("Nummeret er allerede registrert, velg et annet nummer")
        except:
            print("Løpernummeret må være et heltall")
            

navn = {nummer: navn for nummer, navn in zip(nummer, navn)} # Bruker zip til å sette navn inn i et dictionary

print("")

while True:  # Spør etter løpstype
    type = str(input("Har du et løp eller en cup: ")).lower()
    if type in ["cup", "løp"]:
        break
    else:
        print('Du må skrive "løp" eller "cup"')

print("")

if type == "løp": 
    tider = []

    for i in nummer: # Spør etter tider til hvert nummer
        while True:
            try:
                tider.append(float(input(f"Hva ble tiden til løper {i}: ")))
                break
            except:
                print("Du må oppgi et tall!")

    tider = {nummer: tider for nummer, tider in zip(nummer, tider)} # Bruker zip til å sette alle tidene sammen med numrene

    nummer = sortnummer(nummer, list(tider.values()))

    print("\n Rangeringen blir:")  # Lager en rangeringstabell
    p = 1
    for i in nummer:
        print(f"{p}.    {navn[i]}:      {tider[i]}") 
        p+=1   

    
elif type == "cup":
    tider = [[],[],[],[],[]]  # Lager en subliste for hver av løpene i cupen

    for j in range(len(tider)): # Fyller ut listene i listen med tider
        for i in nummer:
            while True:
                try:
                    tider[j].append(float(input(f"Hva ble tiden til løper {i} i runde {j+1}: ")))
                    break
                except:
                    print("Du må oppgi et tall!")
    sumtider = []
    for i in range(len(nummer)):  # Lager en summeringsliste med en indeks for hver løper
        sumtider.append(0)

    for j in range(len(tider)):  # Fyller ut summeringslista med hver tid fra hver løper
        for i in range(len(tider[j])):
            sumtider[i] += tider[j][i]

    sumtider = {nummer: sumtider for nummer, sumtider in zip(nummer, sumtider)} # Bruker zip til å sette alle totaltidene in i et dictionary med navn

    nummer = sortnummer(nummer, list(sumtider.values())) 

    print("\n Rangeringen blir:") # Setter opp rangeringsskema
    p=1
    for i in nummer:
        print(f"{p}.    {navn[i]}:      {sumtider[i]}")
        p+1
