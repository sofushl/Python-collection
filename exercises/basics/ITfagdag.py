def check(inp,corr,acc):
    n = input(inp)
   
    while acc(n):
        print(corr)
        n = input(inp)
    
    return int(n)

while True:

    mode = check("Hvilken oppgave (1, 2, 3 eller 4): ", "Skriv et heltall mellom 1 og 4", lambda n: not n in ("1","2","3","4"))

    if mode == 1:
        n = check("Velg tall n å summere opp til: ", "Skriv et heltall over null", lambda n: not (n.isnumeric() and int(n) > 0))
        res = (n+n**2)/2
        print("Resultatet blir:", res)

    elif mode == 2:
        n = check("Velg et tall n å finne gangetabellen til: ", "Skriv et heltall", lambda n: not n.isnumeric())
        
        for i in range(1, 13):
            print(n*i)

    elif mode == 3:
        text = input("Skriv noe: ").lower()
    
        textl = sorted(list(text))

        charlib = {
            "ingen":0,
            "a":0,
            "d":0
        }

        last = -1

        for i in range(len(textl)-1):
            if textl[i] != textl[i+1]:
                charlib[textl[i]] = i-last
                last = i
        charlib[textl[-1]] = len(textl)-last-1
        
        biggest = "ingen"
        for i in charlib.keys():
            if charlib[i] > charlib[biggest]:
                biggest = i
            elif charlib[i] == charlib[biggest]:
                biggest = "ingen"
                charlib["ingen"] = charlib[i]

        print(f"Det er {charlib['a']} a'er, {charlib['d']} d'er og flest {biggest if biggest != ' ' else 'mellomrom'}!")

    elif mode == 4:
        h = check("Oppgi en sylinderhøyde i desimeter: ","Svaret må være et naturlig tall...",lambda n: isinstance(n, float))
        r = check("Oppgi en sylinderradius i desimeter: ","Svaret må være et naturlig tall...",lambda n: isinstance(n, float))
        
        print(f"Sylinderern din er {3.1415*h*r**2} dm^2")
        
    stop = input("Vil du fortsette?(y/n): ")
   
    while not stop == 'n'or not stop == 'y':
        print("Svaret må være y/n:")
        stop = input("Vil du fortsette?(y/n): ")
    if stop in ("n"):
        break