l = str(input("gi en liste: "))
l = l.split()

for i in range(len(l)):
    l[i] = int(l[i])


def minnum(l):
    m = l[0]
    for i in range(len(l)):
        if m > l[i]:
            m = l[i]
    return m

def minplace(l):
    m = minnum(l)
    p = []
    for i in range(len(l)):
        if l[i] == m:
            p.append(i)
    return p
print (f"Minste tall er {minnum(l)} og det er på plass {minplace(l)}")
