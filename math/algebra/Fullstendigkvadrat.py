a = float(input("a = ")) #spør brukeren om og lagrer et tall i variablen a som en float (tallet skal være a fra en andregradslikning)
b = float(input("b = ")) #samme som før bare tallet b
c = float(input("c = ")) #samme som før bare tallet c

d = b**2 - 4*a*c #regner ut og setter variablen d som resultatet av delen av andregradslikningen som er under kvadratrot

if d == 0: #her sto det bare "if" men for at den skal sjekke om den intastede funksjon er et fulstendig kvadrat skal den bare sjekke om d er 0 (fordi når tallene under kvadratrota er lik 0 blir det bare en løsning på x)
    print ("du har et fullstendig kvadrat!") #printer "du har et fullstendig kvadrat!" om linjen over resulterte i True
else: #om den siste "if" eller "elif" returnerte "False" eksekveres denne
    print ("Dette er nokk ikke et fullstendig kvadrat.") #printer "Dette er nokk ikke et fullstendig kvadrat."
