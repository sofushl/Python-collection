#Oppgave 1.26 Sinus R2

def a(n):
    return 2*n**2

sum_n = 15

s = 0

for i in range(1, sum_n+1):
    s+= a(i)

print(s)
