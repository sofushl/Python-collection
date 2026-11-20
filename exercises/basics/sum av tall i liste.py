l = str(input("gi en liste: "))
l = l.split()
s = 0

for i in range(len(l)):
    l[i] = int(l[i])

print (l)

for i in l:
    s += i

print (f"Summen av tallene i listen er {s}")
print (f"fasit {sum(l)}")

