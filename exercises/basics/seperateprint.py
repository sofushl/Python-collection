nsfig = 0  # Mengden i figurnummer x
nstot = 0  # Mengden nonstop totalt
s = 6      # Startmengden nonstop
p = 4      # Mengden ny nonstop per figur
num = 0

print ("Figurnummer             Non Stop i figur        Non Sop  totalt")

while nstot < 2000:

    num +=1
    nsfig = 6 + p*num
    nstot += nsfig

    print(num, nsfig, nstot, sep = "\t\t\t")

