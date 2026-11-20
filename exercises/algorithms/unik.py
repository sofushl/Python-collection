liste = list(input().split())

if liste[0] == liste[1] or liste[0] == liste[2]:
    wrong = liste[0]
else:
    wrong = liste[1]


for i in liste:
    if i != wrong:
        u = i
        break

print(u)
