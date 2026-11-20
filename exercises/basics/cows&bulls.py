from random import randint

n = []

for i in range(4):
    n.append(int(randint(0, 9)))


def evaluate(n, a):
    c = int(0)
    b = int(0)
    nrem = []
    arem = []

    for t in range(4):
        if a[t] == n[t]:
            c = c + 1
        else:
            nrem.append(n[t])
            arem.append(a[t])
            
    for i in arem:
        if i in nrem:
            b = b + 1
            nrem.remove(i)
    return (c, b)


def test():
    c, b = evaluate([1, 2, 3, 4], [2, 3, 4, 5])
    if c != 0 or b != 3:
        print ()
    
    
while True:
    a = str(input("guess the 4 digit number: "))
    a = [int(i) for i in a]

    c, b =evaluate(n, a)

        
    print ("Bulls: " + str(b) + " Cows: " + str(c))
    if c == 4:
        break

print (a, "is correct!")

