l = str(input("gi en liste: "))
l = l.split()

for i in range(len(l)):        
    l[i] = int(l[i])


def primedetector(num):
    for i in range(2, int(round(num/1.5))):
        print (i)
        if num%i == 0:
            return False
    return True

p = []

for i in l:
    if primedetector(i) == True:
        p.append(i)
print(f"Primtallene er {p}")
