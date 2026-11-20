t = int(input("hva er teller: "))
n = int(input("hva er nevner: "))

d = True

if t > n:
    b = t
elif n > t:
    b = n
elif n == t:
    print ("Faktoriserte brøk bli 1 delt på 1")
    d = False

b = b // 2 + 1

if d:
    for i in range(2, b):
        print (i, b, n, t)
        if (n % i) == 0 and (t % i) == 0:
            n = n / i
            t = t / i
            
    print ("Faktoriserte brøk blir ", t, " delt på ", n)
