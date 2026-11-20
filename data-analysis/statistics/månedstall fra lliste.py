m = "JanFebMarAprMaiJunJulAugSepOktNovDes"


split_l =[]

for i in range(len(m)):
    if m[i].upper() == m[i]:
        split_l.append(i)

m_l =[]

for i in range(len(split_l)-1):
    m_l.append(m[split_l[i]:split_l[i+1]])

m_l.append(m[split_l[i+1]:])

t = int(input())

print(m_l[t-1])


